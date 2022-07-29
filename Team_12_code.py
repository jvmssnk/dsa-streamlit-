import streamlit as st
import timeit
# import warnings
import heapq
# warnings.filterwarnings("ignore")
# st.set_page_config(layout="wide")
heade=st.container()
deatil=st.container()
with heade:
    ori = '<p style="font-family:Sans serif; color:#ff3300; font-size: 60px;"><u>DESIGN AND ANALYSIS OF ALGORITHM</u></p>'
    st.markdown(ori,unsafe_allow_html=True)
with deatil:
    orii = '<p style="font-family:Sans serif; color:cyan; font-size: 40px;"><u>PROBLEM DESCRIPTION :</u></p>'
    st.markdown(orii,unsafe_allow_html=True)
    orii2 = '<p style="font-family:Sans serif; color: #ff00ff; font-size: 25px;text-transform: uppercase;">Minimum Number of Refueling Stops</p>'
    st.markdown(orii2,unsafe_allow_html=True)
    ori1 = '<p style="font-family:ans-serif; color:yellow; font-size: 22px;text-align: justify;">A car travels from a starting position to a destination which is target miles east of the starting position. There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived</p>'
    st.markdown(ori1,unsafe_allow_html=True)
def mi(target, fuel, s):
        heap = [] 
        s = [(0, 0)] + s + [(target, 0)]
        print(s)
        print(len(s))
        n, ans = len(s), 0
        for i in range(1, n):
            fuel -= s[i][0] - s[i-1][0]
            while heap and fuel < 0:
                fuel -= heapq.heappop(heap)
                ans += 1
            if fuel < 0: return -1
            heapq.heappush(heap, -s[i][1])
        return ans
def minr(target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1
tar= (st.number_input(label="INSERT A NUMBER FOR TARGET",step=1))
sta= st.number_input(label="START FUEL",step=1)
s=st.text_input('ENTER IN STRING FORMAT')
s1=st.text_input(' DYNAMIC OR GREEDY APPROCH TYPE IN SMALL')
s=s.split(',')
n=[]
for i in range(0,len(s)):
    l=s[i].split()
    for i in range(0,len(l)):
        l[i]=int(l[i])
    n.append(l)
if (st.button('SUBMIT')):
    if s1=='greedy':
        start = timeit.default_timer()
        k=mi(tar,sta,n)
        stop = timeit.default_timer()
        st.write('Time IN GREEDY APPROCH: ',( stop - start))
        st.write('no of stops required GREEDY APPROCH:', k)
    else:
        start = timeit.default_timer()
        k1=minr(tar,sta,n)
        stop = timeit.default_timer()
        st.write('Time IN DYNAMIC APPROCH: ',( stop - start))
        st.write('no of stops required DYNAMIC APPROCH:', k1)







