import math
import matplotlib.pyplot as plt


class Gaussian():
    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):

        avg = 1.0 * sum(self.data) / len(self.data)

        self.mean = avg

        return self.mean

    def calculate_stdev(self, sample=True):

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean

        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)

        self.stdev = sigma

        return self.stdev

    def read_data_file(self, file_name, sample=True):

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

    def pdf(self, x):
        return (1.0/(self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((X - self.mean) / self.stdev) ** 2)

    def plot_histogram_pdf(self, n_spaces=50):

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        interval = 1.0 * (max_range - min_range) / n_spaces
        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x,y)
        axes[1].set_title('Normal Distribution for \n Sample mean and Sample Standard Devieation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x,y
