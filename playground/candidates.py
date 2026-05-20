for llambda in range(16, 33):
    for pi, theta in [(226, 5), (116, 3)]:
        llambda_prime = pi % llambda
        kappa = theta * (1 << (llambda - llambda_prime))
        print(f"lambda {llambda}, |kappa| {kappa.bit_length():2}")
    print("-----")
