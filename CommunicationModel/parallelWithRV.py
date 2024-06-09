
import math


def combination(n, k): 
    # 计算组合数
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def parallelWithRV(p,n,k):
    # the probability exactly k-1  non-auctioneers communicate a bid to the auctioneer
    result = p**(2*(k-1))*(p*(1-p)+(1-p))**(n-k)*combination(n-1,k-1)
    return result

def parallelWithRV_l(p,n,k):
    # less than k-1 non-auctioneers communicate a bid to the auctioneer, including k-1
    result = 0
    for i in range(1,k+1):
        result += parallelWithRV(p,n,i)
    return result

def expectedWonItems(m,p,n,k):
    expectedSum = 0
    for i in range(1,n+1):
        expectedSum += m/k*parallelWithRV(p,n,k)
    return expectedSum

def main():
    p = 0.8
    m = 10     # number of items
    n = 10    # number of agents
    k = 8     # number of non-auctioneers communicate a bid to the auctioneer
    # k in [1,n]
    print("The number of agents is: ",n)
    print("The number of items is: ",m)
    print("The Bernoulli model p is: ",p)
    print("The probability exactly {} non=auctioneers coomunicate a bid to the auctioneer is: {:.3f}".format(k-1,parallelWithRV(p,n,k)))
    print("The probability <= {} non=auctioneers coomunicate a bid to the auctioneer is: {:.3f}".format(k-1,parallelWithRV_l(p,n,k)))
    print(expectedWonItems(m,p,n,k))

if __name__ == '__main__':
    main()

