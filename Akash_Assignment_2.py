# Notice: do not change these function name
def is_palindrome(a):
    if (str(a) == str(a)[::-1]):
        return True
    else:
        return False    
    
def is_anagrams(s, t):
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    else:
        return False
    pass

def top_k_words(p,k):
    from collections import Counter
    noise = ['.',';',',']
    for i in p:
        if i in noise:
            p=p.replace(i, '')
    word_list = list(p.split(" "))          
    freq = Counter(word_list)
    most_repeated = freq.most_common(k)
    return [item for item,word_list in most_repeated]
    pass
   
def gradient_descent(x, y, m, c, epochs, L=0.001):
    for e in range(epochs):
        Dm = []
        Dc = []
        for e in range(len(x)):
            yp = (m*x[e][0]) + c
            Dm.append ((x[e][0] * (yp - y[e])))
            Dc.append ((yp - y[e]))
        dm = sum(Dm)/len(Dm)
        dc = sum(Dc)/len(Dc)
        m = m - L * dm  
        c = c - L * dc  
    return (m, c)
    pass
    
#

if __name__ == "__main__":  
    
    # Test Question 1
    
    print("\nQ1")
    q1_test1 = 121
    q1_test2 = -121
    q1_test3 = 0
    q1_answer1 = is_palindrome(q1_test1)
    q1_answer2 = is_palindrome(q1_test2)
    q1_answer3 = is_palindrome(q1_test3)
    print(q1_answer1 )
    print("right answer: True")
    print("--------------")
    print(q1_answer2)
    print("right answer: False")
    print("--------------")
    print(q1_answer3)
    print("right answer: True")

    
    print("\nQ2")
    q2_test1_s = "anagram"
    q2_test1_t = "nagaram"
    q2_answer1 =  is_anagrams(q2_test1_s, q2_test1_t)
    print(q2_answer1)
    print("right answer: True")

    print("--------------")
    q2_test2_s = "python"
    q2_test2_t = "py"
    q2_answer2 =  is_anagrams(q2_test2_s, q2_test2_t)
    print(q2_answer2)
    print("right answer: False")
    print("--------------")

    # test question 3
    print("\nQ3")
    q3_test1_s =  "i love python, he love coding python. the course is about python. "
    q3_test1_k = 2
    q3_answer = top_k_words(q3_test1_s, q3_test1_k)
    print(q3_answer)
    print("right: answer:")
    print("['python', 'love']")

    print ("\nQ4")

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    m = 0
    c = 0
    q4_epochs200 = 200
    q4_epochs500 = 500
    q4_epochs1000 = 1000
    q4_epochs2000 = 2000
    q4_epochs3000 = 3000
    q4_answer1 = gradient_descent(x,y,m,c,q4_epochs200)
    q4_answer2 = gradient_descent(x,y,m,c,q4_epochs500)
    q4_answer3 = gradient_descent(x,y,m,c,q4_epochs1000)
    q4_answer4 = gradient_descent(x,y,m,c,q4_epochs2000)
    q4_answer5 = gradient_descent(x,y,m,c,q4_epochs3000)
    print(q4_answer1)
    print("right answer:")
    print("17.724810647355827, 22.97599012903927")
    print("--------------")
    print(q4_answer2)
    print("right answer:")
    print("35.97890301691016, 46.54235227399102")
    print("--------------")
    print(q4_answer3)
    print("right answer:")
    print("52.816639894324545, 68.05971340716786")
    print("--------------")
    print(q4_answer4)
    print("right answer:")
    print("64.56549666509812, 82.46678636085996")
    print("--------------")
    print(q4_answer5)
    print("right answer:")
    print("67.42648874428104, 85.32444456113602")
    print("--------------")