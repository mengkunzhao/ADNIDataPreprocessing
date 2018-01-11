__author__ = 'Haohan Wang'

import numpy as np

def generateFinalData():
    snps = []
    phenos = []

    sample2pheno = np.load('../result/phenoDic.npy').item()
    # print type(sample2pheno)
    sample2index = {}
    sampleList = np.load('../result/sampleID.npy')
    for i in range(len(sampleList)):
        sample2index[sampleList[i][1]] = i

    snpAll = np.load('../result/snpData.npy')

    for s in sample2pheno:
        phenos.append(sample2pheno[s])
        snps.append(snpAll[sample2index[s],:])

    phenos = np.array(phenos)
    snps = np.array(snps)

    print phenos.shape
    print snps.shape

    np.save('../final/pheno', phenos)
    np.save('../final/snps', snps)

if __name__ == '__main__':
    generateFinalData()