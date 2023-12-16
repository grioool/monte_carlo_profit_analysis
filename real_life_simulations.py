import numpy as np

def box_color_ball_probability():
    prob_blue_first = np.divide(7, 12)
    prob_red_second = np.divide(5, 11)
    prob_blue_third = np.divide(6, 10)
    prob_red_fourth = np.divide(4, 9)

    overall_prob = prob_blue_first * prob_red_second * prob_blue_third * prob_red_fourth
    return overall_prob

def birthday_problem():
    prob_unique_birthdays = 1.0
    people = 0

    while prob_unique_birthdays > 0.5:
        people += 1
        prob_unique_birthdays *= np.divide(365 - people + 1, 365)

    return people


def main():
    probability = box_color_ball_probability()
    print("Probability for Box Color Ball Problem:", probability)

    people_needed = birthday_problem()
    print("Number of people needed for a 50% chance of shared birthdays:", people_needed)

if __name__ == "__main__":
    main()
