# Day 07 - Bayes Theorem Solution

P_disease = 0.01
P_no_disease = 0.99

P_pos_given_disease = 0.99
P_pos_given_no_disease = 0.01

P_positive = (P_pos_given_disease * P_disease) + (P_pos_given_no_disease * P_no_disease)

P_disease_given_positive = (P_pos_given_disease * P_disease) / P_positive

print("P(Disease | Positive):", round(P_disease_given_positive, 4))
