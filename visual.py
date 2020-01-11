import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

fpred =open('red.txt','rb')
fpred1 =open('red1.txt','rb')
pr = fpred.readlines()
preRed = [ int(i) for i in pr[0].split()]
pr1 = fpred1.readlines()
postRed = [ int(i) for i in pr1[0].split()]
preRed = pd.DataFrame(preRed, columns=['values'])
postRed = pd.DataFrame(postRed, columns=['values'])
preRed.reset_index()
postRed.reset_index()

sns.lineplot(data=preRed[:50])

sns.lineplot(data=postRed[:50])

fpgreen =open('green.txt','rb')
fpgreen1 =open('green1.txt','rb')
pr = fpgreen.readlines()
preGreen = [ int(i) for i in pr[0].split()]
pr1 = fpgreen1.readlines()
postGreen = [ int(i) for i in pr1[0].split()]
preGreen = pd.DataFrame(preGreen, columns=['values'])
postGreen = pd.DataFrame(postGreen, columns=['values'])
preGreen.reset_index()
postGreen.reset_index()

sns.lineplot(data=preGreen[:50])

sns.lineplot(data=postGreen[:50])

fpblue =open('blue.txt','rb')
fpblue1 =open('blue1.txt','rb')
pr = fpblue.readlines()
preBlue = [ int(i) for i in pr[0].split()]
pr1 = fpblue1.readlines()
postBlue = [ int(i) for i in pr1[0].split()]
preBlue = pd.DataFrame(preBlue, columns=['values'])
postBlue = pd.DataFrame(postBlue, columns=['values'])
preBlue.reset_index()
postBlue.reset_index()

sns.lineplot(data=preBlue[:50])

sns.lineplot(data=postBlue[:50])