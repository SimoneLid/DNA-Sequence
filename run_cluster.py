import subprocess
import os


TEST = ["omp"]  # versioni da eseguire
NUM_ITER = 10
NUM_MACHINE = ["4"]   # n nodi cluster con cui eseguire (ognuno con 32 core)
NUM_THREAD_OMP = ["4","16","32"]   # n thread OpenMP con cui eseguire
TIME_ROUND=6   # cifre decimali dei tempi

# ARGS
SEQ_LENGTH='10000'
PROB_G='0.35'
PROB_C='0.2'
PROB_A='0.25'
PAT_RNG_NUM='0'
PAT_RNG_LENGTH_MEAN='0'
PAT_RNG_LENGTH_DEV='0'
PAT_SAMPLES_NUM='10000'
PAT_SAMP_LENGTH_MEAN='9000'
PAT_SAMP_LENGTH_DEV='9000'
PAT_SAMP_LOC_MEAN='50'
PAT_SAMP_LOC_DEV='100'
PAT_SAMP_MIX='M'
LONG_SEED='4353435'

ARGS=[SEQ_LENGTH,PROB_G,PROB_C,PROB_A,PAT_RNG_NUM,PAT_RNG_LENGTH_MEAN,PAT_RNG_LENGTH_DEV,PAT_SAMPLES_NUM,PAT_SAMP_LENGTH_MEAN,PAT_SAMP_LENGTH_DEV,PAT_SAMP_LOC_MEAN,PAT_SAMP_LOC_DEV,PAT_SAMP_MIX,LONG_SEED]

# converte stdout del programma in c nei valori che ci interessano
def convert_stdout(stdout):
    values=stdout.decode("utf-8").split()
    time=float(values[1])
    pat_matches=int(values[3].replace(",",""))
    checksum_found=int(values[4].replace(",",""))
    checksum_matches=int(values[5])
    return time,pat_matches,checksum_found,checksum_matches

def convert_mpi_output(text):
    values=text.split()
    time=float(values[1])
    pat_matches=int(values[3].replace(",",""))
    checksum_found=int(values[4].replace(",",""))
    checksum_matches=int(values[5])
    return time,pat_matches,checksum_found,checksum_matches

# scrivi i tempi medi su file
def write_times(times,filename):
    with open(filename,"w") as F:
        for k,e in times.items():
            if k=="seq":
                mean_seq=round(sum(e)/len(e),TIME_ROUND)
                F.write(k+": "+str(mean_seq)+"\n")
            else:
                F.write(k+"\n")
                for n,l in e.items():
                    curr_mean_time=round(sum(l)/len(l),TIME_ROUND)
                    F.write(n+": "+str(curr_mean_time))
                    F.write("     speedup:"+str(round(mean_seq/curr_mean_time,TIME_ROUND)))
                    F.write("\n")
            F.write("--------------------------------\n")
    return



# dict con tutti i tempi
times={"seq":[]}

# runna il sequenziale
for i in range(NUM_ITER):
    print("----------------------------------------------------")
    print("Programma: sequenziale   iterazione:",i)
    stdout=subprocess.check_output(['./align_seq']+ARGS)
    time, pat_matches, checksum_found, checksum_matches = convert_stdout(stdout)
    times["seq"].append(time)

# runna mpi
if "mpi" in TEST:
    times["mpi"]={}
    for n in NUM_MACHINE:
        times["mpi"][str(32*int(n))]=[]
        for i in range(NUM_ITER):
            print("----------------------------------------------------")
            print("Programma: mpi  n rank:",32*int(n)," iterazione:",i)
            stdout=subprocess.check_output(['condor_submit',f'jobs/job{n}.job'])
            while(os.path.isfile("logs/out.0")!=True):
                continue
            with open("logs/out.0") as F:
                text=F.read()
            os.remove("logs/out.0")
            time, pat_matches, checksum_found, checksum_matches = convert_mpi_output(text)
            times["mpi"][n].append(time)

# runna omp
if "omp" in TEST:
    times["omp"]={}
    for n in NUM_THREAD_OMP:
        times["omp"][n]=[]
        for i in range(NUM_ITER):
            print("----------------------------------------------------")
            print("Programma: omp  n rank:",n," iterazione:",i)
            stdout=subprocess.check_output(['./align_omp']+ARGS+[n])
            time, pat_matches, checksum_found, checksum_matches = convert_stdout(stdout)
            times["omp"][n].append(time)


print(times)
write_times(times,"times.txt")