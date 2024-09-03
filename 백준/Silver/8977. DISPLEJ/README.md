# [Silver V] DISPLEJ - 8977 

[문제 링크](https://www.acmicpc.net/problem/8977) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 9월 3일 14:16:58

### 문제 설명

<p>The game "display" is gaining popularity in casinos around the world. The game is run on a big screen visible to all players. A single integer is displayed on the screen, which changes every minute. </p>

<p>The players attempt to determine the sum of K consecutive numbers, starting from the B-th displayed number. More precisely, if X<sub>n</sub> is the n-th number displayed (starting with X<sub>1</sub>), then players try to determine the sum X<sub>B</sub> + X<sub>B+1</sub> + ... + X<sub>B+K−1</sub>. </p>

<p>Mirko is thrilled with this game and often spends five or six hours calculating sums and growing in debt. Recently he realized that the numbers on screen follow a precise pattern; the same sequence of N integers repeats over and over. </p>

<p>Help Mirko to find the sought sum, given the sequence of number repeating. </p>

### 입력 

 <p>The first line contains three integers N, K and B, 1 ≤ N ≤ 100, 1 ≤ K ≤ 100, 1 ≤ B ≤ 10<sup>9</sup>. </p>

<p>The second line contains N non-negative integers less than 100, separated by spaces. This is the sequence that keeps repeating on screen. </p>

### 출력 

 <p>Output the sum on a single line. </p>

