def calculate_true_relationship(s1, s2, name):
    f = open("true_relationship/true_relationship_" + name + ".txt", "a")

    # s1_s2
    if name == "s1_s2":
        for i in range(len(s1)):
            player = s1[i].rsplit('/')[-1].lower()
            for j in range(len(s2)):
                player2 = s2[j].rsplit('/')[-2].lower()
                if player == player2:
                    f.write("P 1 {} P 2 {}".format(i + 1, j + 1))
                    f.write("\n")

    # s1_s3
    if name == "s1_s3":
        for i in range(len(s1)):
            player = s1[i].rsplit('/')[-1].lower()
            for j in range(len(s2)):
                player2 = s2[j].rsplit('/')[-3].lower()
                if player == player2:
                    f.write("P 1 {} P 3 {}".format(i + 1, j + 1))
                    f.write("\n")

    # s2_s3

    if name == "s2_s3":
        for i in range(len(s1)):
            player = s1[i].rsplit('/')[-2].lower()
            for j in range(len(s2)):
                player2 = s2[j].rsplit('/')[-3].lower()
                if player == player2:
                    f.write("P 2 {} P 3 {}".format(i + 1, j + 1))
                    f.write("\n")

    f.close()


def calculate_precision(name):
    with open("output/associazioni_" + name + ".txt") as f:
        retrieved = f.read().splitlines()
    with open("true_relationship/true_relationship_" + name + ".txt") as f2:
        relevant = f2.read().splitlines()

    for k in range(len(retrieved)):
        retrieved[k] = retrieved[k].replace(" ", "")

    for j in range(len(relevant)):
        relevant[j] = relevant[j].replace(" ", "")

    numeratore = 0
    for i in range(len(retrieved)):
        if retrieved[i] in relevant:
            numeratore += 1
    precision = numeratore / len(retrieved)
    print("Precision " + name + " : " + str(precision))
    return precision


def calculate_recall(name):
    with open("output/associazioni_" + name + ".txt") as f:
        retrieved = f.read().splitlines()
    with open("true_relationship/true_relationship_" + name + ".txt") as f2:
        relevant = f2.read().splitlines()

    for k in range(len(retrieved)):
        retrieved[k] = retrieved[k].replace(" ", "")

    for j in range(len(relevant)):
        relevant[j] = relevant[j].replace(" ", "")

    numeratore = 0
    for l in retrieved:
        if l in relevant:
            numeratore += 1
    recall = numeratore / len(relevant)
    print("Recall " + name + " : " + str(recall))
    return recall


def calculate_f1(name):
    precision = calculate_precision(name)
    recall = calculate_recall(name)
    f1 = (2 * precision * recall) / (precision + recall)
    print("F1 " + name + " : " + str(f1))
