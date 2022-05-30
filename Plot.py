from matplotlib import pyplot as plt

def plot(L1, lab1, L2, lab2, title, ylabel1 = None, ylabel2 = None, xlabel = 'Iteration'):
    
    if (ylabel2 == None): 
        plt.close()
        plt.semilogy(L1, color = 'red', label = lab1)
        plt.semilogy(L2, color = 'blue', label = lab2)
        plt.xlabel(xlabel, fontsize = 15)
        plt.ylabel(ylabel1, fontsize = 15)
        plt.title(title, fontsize = 17)
        plt.grid(which = 'both')
        plt.legend(loc='upper right', fancybox=True, prop={'size':13}).get_frame().set_alpha(0.4)
        plt.show()
    else: 
    # First Figure 
        plt.close()
        plt.semilogy(L1, color = 'red', label = lab1)
        plt.xlabel(xlabel, fontsize = 15)
        plt.ylabel(ylabel1, fontsize = 15)
        plt.title(title, fontsize = 17)
        plt.grid(which = 'both')
        plt.legend(loc='upper right', fancybox=True, prop={'size':13}).get_frame().set_alpha(0.4)
        plt.show()
    # Second Figure 
        plt.close()
        plt.semilogy(L2, color = 'blue', label = lab2)
        plt.xlabel(xlabel, fontsize = 15)
        plt.ylabel(ylabel2, fontsize = 15)
        plt.title(title, fontsize = 17)
        plt.grid(which = 'both')
        plt.legend(loc='upper right', fancybox=True, prop={'size':13}).get_frame().set_alpha(0.4)
        plt.show()