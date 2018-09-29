import random
import numpy as np
import matplotlib.pyplot as plt

class secuencia:
    def __init__(self ,seq,seq_type = "DNA"):
        self.seq = seq
        self.seq_type = seq_type
    def __eq__(self,s2):
        if self.seq==s2.seq:
            return True
        else:
            return False
    def ver(self):
        print("Secuencia:%s"%self.seq)
    def contar_nucleotidos(self):
        nuc=["A","G","C","T"]
        num={}
        for x in nuc:
            num[x]=(self.seq.count(x)/len(self.seq))
        return num
    def random(self,n):
        nuc=["A","G","C","T"]
        seq=""
        for i in range(n):
            seq+=(random.choice(nuc))
        self.seq=seq          
        return seq
    def plot_Fraction(self):
        fig, ax = plt.subplots()
        p=self.contar_nucleotidos()
        x=[1,2,3,4]
        barlist=plt.bar(x,p.values(),edgecolor="black",alpha=0.8)
        ax.set_xticks(x)
        ax.set_xticklabels(['A', 'G', 'C','T'])
        
        barlist[0].set_facecolor("g")
        barlist[1].set_facecolor("y")
        barlist[2].set_facecolor("b")
        barlist[3].set_facecolor("r")
        plt.xlabel("Nucleótidos")
        plt.ylabel("Fracción")
        plt.title("Distribución de Nucleótidos")
        plt.show()
        return
    def compara_secuencia(self,s2):
        n=len(self.seq)
        m=len(s2.seq)
        mat=np.zeros((m,n),dtype=int)
        print(mat.shape)
        for i in range(0,n):
            for j in range(0,m):
              if self.seq[i:i+3]==s2.seq[j:j+3]:
                mat[j,i]=1
        x=np.arange(n)
        y=np.arange(m)
        XX,YY=np.meshgrid(x,y)
        plt.contour(XX,YY,mat)
        plt.show()
        return mat    