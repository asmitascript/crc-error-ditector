# CRC Error Detection Simulator

## Overview

The CRC Error Detection Simulator is a Python-based project that demonstrates the working of the Cyclic Redundancy Check (CRC) algorithm, one of the most widely used error detection techniques in digital communication systems. The simulator generates CRC bits for a given data stream, appends them to the original data, simulates transmission, and verifies whether the received data contains any transmission errors.

This project helps students and beginners understand how CRC ensures data integrity during communication between devices and networks.

---

## Problem Statement

During data transmission, information can become corrupted due to noise, interference, hardware failures, or signal distortion. To ensure reliable communication, error detection mechanisms are required.

This project implements the Cyclic Redundancy Check (CRC) algorithm to detect transmission errors by generating and validating CRC codes using modulo-2 division. The simulator determines whether the received data is error-free or contains errors.

---

## Objectives

* Understand the concept of CRC error detection.
* Implement the CRC algorithm using Python.
* Simulate data transmission and reception.
* Detect transmission errors using CRC verification.
* Study the practical applications of CRC in communication systems.

---

## Features

* CRC code generation
* Binary modulo-2 division implementation
* Data transmission simulation
* Error detection at the receiver side
* Interactive console-based interface
* Educational and beginner-friendly implementation
* Lightweight and easy to run

---

## Applications

CRC is commonly used in:

* Computer Networks
* Ethernet Communication
* Wireless Networks
* Data Storage Devices
* Embedded Systems
* Satellite Communication
* Mobile Communication Systems
* Digital Communication Networks

---

## Technology Stack

| Component               | Technology        |
| ----------------------- | ----------------- |
| Programming Language    | Python 3          |
| Version Control         | Git               |
| Repository Hosting      | GitHub            |
| Development Environment | VS Code / PyCharm |

---

## Project Structure

```text
CRC-Error-Detection-Simulator/
│
├── README.md
├── crc.py
├── Project_Report.pdf
└──flowchart.jpeg
```

---

## CRC Working Principle

### Sender Side

1. Input binary data.
2. Input generator polynomial.
3. Append (n−1) zeros to the data.
4. Perform modulo-2 division.
5. Generate CRC remainder.
6. Append CRC bits to the original data.
7. Transmit the complete frame.

### Receiver Side

1. Receive transmitted frame.
2. Perform modulo-2 division using the same generator polynomial.
3. Check the remainder.
4. If the remainder is all zeros:

   * No Error Detected.
5. Otherwise:

   * Error Detected.

---

## Flow Diagram

```text
START
   |
   v
Enter Data Bits
   |
   v
Enter Generator Polynomial
   |
   v
Append Zeroes
   |
   v
Perform CRC Division
   |
   v
Generate CRC
   |
   v
Transmit Data
   |
   v
Receive Data
   |
   v
Perform CRC Check
   |
   v
Is Remainder Zero?
   |        |
  Yes      No
   |        |
No Error  Error Detected
   |
   v
  END
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/asmitascript/crc-error-detector.git
```

### Navigate to the Project Directory

```bash
cd CRC-Error-Detection-Simulator
```

### Run the Program

```bash
python crc_simulator.py
```

---

## Sample Input

```text
Enter Data Bits: 1101011011
Enter Generator Polynomial: 10011
```

## Sample Output

```text
CRC Remainder : 1110

Transmitted Data :
11010110111110
```

### Verification

```text
Enter Received Data:
11010110111110

No Error Detected!
```

### Error Case

```text
Enter Received Data:
11010100111110

Error Detected!
```

---

## Algorithm

### CRC Generation

1. Append zeros equal to (length of divisor − 1).
2. Divide the data using modulo-2 division.
3. Obtain the remainder.
4. Append the remainder to the original data.

### CRC Verification

1. Divide received data using the same divisor.
2. Check the final remainder.
3. If all bits are zero, data is valid.
4. Otherwise, an error is detected.

---

## Time Complexity

Let:

* n = Length of data bits
* m = Length of generator polynomial

### CRC Generation
O(n × m)


### CRC Verification
O(n × m)

### Space Complexity
O(n)

## Learning Outcomes

After completing this project, users will be able to:

* Understand CRC error detection techniques.
* Learn modulo-2 binary division.
* Implement networking concepts in Python.
* Analyze algorithm efficiency.
* Gain hands-on experience with Git and GitHub.
* Understand real-world communication protocols.

---

## Team Contributions

### Member 1 (Team Leader)

* Project planning
* CRC algorithm implementation
* Python development
* Testing and debugging
* GitHub repository management
* Documentation

### Member 2

* Research and study of CRC concepts
* Literature review
* Assistance in testing

### Member 3

* Documentation support
* Presentation preparation
* Project review

---

## Future Enhancements

* Develop a graphical user interface (GUI).
* Support multiple CRC standards.
* Visualize each step of CRC division.
* Simulate real network transmission.
* Add file-based CRC verification.
* Implement web-based CRC simulator.

---

## Conclusion

The CRC Error Detection Simulator successfully demonstrates the practical implementation of the Cyclic Redundancy Check algorithm. The project verifies how transmission errors can be detected efficiently using polynomial division and XOR operations. It provides a clear understanding of error detection techniques used in modern communication systems and serves as an educational tool for learning networking and data communication concepts.

---

## References

1. Data Communications and Networking – Behrouz A. Forouzan
2. Computer Networks – Andrew S. Tanenbaum
3. Computer Networking: A Top-Down Approach – Kurose and Ross
4. Python Documentation
5. Git Documentation
6. GitHub Documentation

---

## License

This project is developed for educational and academic purposes.

© 2026 CRC Error Detection Simulator Project Team
