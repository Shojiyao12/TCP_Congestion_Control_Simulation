# TCP Congestion Control Simulation

This project simulates **TCP Congestion Control** mechanisms, illustrating how the **Congestion Window (cwnd)** changes over time in response to network events such as **timeouts, fast retransmissions, slow start, and congestion avoidance**.

## Quickstart Guide

### Running the Simulation
1. Copy all the contents from this repository.
2. Open a terminal and navigate to the folder containing `congestion.py`.
3. Run the program using:
   ```bash
   python congestion.py
   ```
4. The simulation will:
   - Print log entries showing **cwnd** changes due to different congestion control mechanisms.
   - Plot a graph showing how **cwnd** evolves over **Round Trip Times (RTTs)**.

## Core Concepts
- **Slow Start**: Doubles `cwnd` until it reaches `ssthresh`.
- **Congestion Avoidance**: Increases `cwnd` linearly after `ssthresh` is reached.
- **Timeouts**: Drops `cwnd` to `1` and updates `ssthresh`.
- **Fast Retransmit**: Quickly reduces `cwnd` but avoids a full restart.

## Preview of Simulation Output

### **Log Output Example**
```bash
Slow start at RTT 0: cwnd=2, ssthresh=16
Slow start at RTT 1: cwnd=4, ssthresh=16
Congestion avoidance at RTT 5: cwnd=17, ssthresh=16
Timeout at RTT 10: cwnd=1, ssthresh=8
...
```

### **Graph Example**
The simulation generates a graph plotting `cwnd` over **RTTs**, illustrating how congestion control operates dynamically.

![TCP Congestion Control Graph](https://drive.google.com/file/d/1h3PbwQRr5H0q0HqaECi8XInHuPKsL1z8/view?usp=sharing)

## Notes:
- The probability of **timeouts** and **fast retransmits** is configurable within the script.
- The initial `ssthresh` value can be modified to observe different behaviors.
- The model follows the fundamental principles of **TCP Tahoe & Reno** congestion control.

## Future Enhancements
- Implement **Selective Acknowledgments (SACK)** for a more advanced simulation.
- Add real-world **network trace integration**.
- Extend support for **TCP Cubic**.

---


