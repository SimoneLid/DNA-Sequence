import subprocess
import os

TEST = ["omp"]  # versioni da 
NUM_ITER = 10
NUM_THREADS = ["1","2"]   # n thread con cui eseguire
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
pat_matches_seq = 0
checksum_found_seq = 0
checksum_matches_seq = 0

# runna il sequenziale
for i in range(NUM_ITER):
    print("----------------------------------------------------")
    print("Programma: sequenziale   iterazione:",i)
    stdout=subprocess.check_output(['./align_seq']+ARGS)
    time, pat_matches_seq, checksum_found_seq, checksum_matches_seq = convert_stdout(stdout)
    times["seq"].append(time)

# runna per gli altri tipi
for program in TEST:
    times[program]={}
    for n in NUM_THREADS:
        times[program][n]=[]
        for i in range(NUM_ITER):
            print("----------------------------------------------------")
            print("Programma:",program,"  n thread:",n," iterazione:",i)
            if program=="mpi":
                stdout=subprocess.check_output(['mpirun','-n',str(n),f'./align_{program}']+ARGS)
            elif program=="omp":
                stdout=subprocess.check_output(['./align_omp']+ARGS+[n])
            time, pat_matches, checksum_found, checksum_matches = convert_stdout(stdout)
            if i==0:
                print(f'Pat matches:',pat_matches)
                print("checksum_found:",checksum_found)
                print("checksum_matches:",checksum_matches)
                if pat_matches!=pat_matches_seq or checksum_found!=checksum_found_seq or checksum_matches!=checksum_matches_seq:
                    print(f'\nErrore!!!\nValori di ritorno non uguali al sequenziale')
            times[program][n].append(time)

print(times)
write_times(times,"times.txt")



            
        


    






