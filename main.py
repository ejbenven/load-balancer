from loadBalancer import LoadBalancer, Provider


if __name__ == "__main__":
    N = 10
    lb = LoadBalancer(N)
    for _ in range(N):
        provider = Provider()
        lb.add_provider(provider)


    for _ in range(10):
        print(lb.get())
