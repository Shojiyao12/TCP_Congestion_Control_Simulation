import random
import matplotlib.pyplot as plt

def simulate_tcp_congestion_control(rtts=100, initial_ssthresh=16):
    cwnd = 1
    ssthresh = initial_ssthresh
    log = []
    cwnd_values = []

    for rtt in range(rtts):
        if random.random() < 0.2:
            action = "Timeout"
            log.append(f"{action} at RTT {rtt}: cwnd={cwnd}, ssthresh={ssthresh}")
            ssthresh = max(cwnd // 2, 2)
            cwnd = 1
            
        else:
            if  random.random() < 0.1:
                action = "Fast retransmit"
                log.append(f"{action} at RTT {rtt}: cwnd={cwnd}, ssthresh={ssthresh}")
                ssthresh = max(cwnd // 2, 2)
                cwnd = ssthresh
            else:   
                if cwnd < ssthresh:
                    action = "Slow start"
                    cwnd *= 2
                    log.append(f"{action} at RTT {rtt}: cwnd={cwnd}, ssthresh={ssthresh}")
        
                else:
                    action = "Congestion avoidance"
                    cwnd += 1
                    log.append(f"{action} at RTT {rtt}: cwnd={cwnd}, ssthresh={ssthresh}")

        cwnd_values.append(cwnd)

    return log, cwnd_values

def main():
    log, cwnd_values = simulate_tcp_congestion_control()

    for entry in log:
        print(entry)

    plt.figure(figsize=(12, 6))
    plt.plot(cwnd_values, label="Congestion Window (cwnd)")
    plt.title("TCP Congestion Control Simulation")
    plt.xlabel("Time (RTTs)")
    plt.ylabel("Congestion Window Size (MSS)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()