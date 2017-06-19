# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.-
    sub_val_work = dict()
    inputFile = open(filename)
    for line in inputFile:
        #print(line)
        #svw = line.replace("\n", "")
        #print(svw)
        svw = line.split(",")
        sub_val_work[svw[0]] = (int(svw[1]), int(svw[2].replace("\n", "")))
        # print line
    return sub_val_work

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

# loadSubjects(SHORT_SUBJECT_FILENAME)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res
# print(loadSubjects(SHORT_SUBJECT_FILENAME).items()[0:5])
# printSubjects(loadSubjects(SUBJECT_FILENAME))
#printSubjects(loadSubjects(SHORT_SUBJECT_FILENAME))
#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[VALUE] > subInfo2[VALUE]


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[WORK] < subInfo2[WORK]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...
    calc = float(subInfo1[VALUE])/subInfo1[WORK] > float(subInfo2[VALUE])/subInfo2[WORK]
    print("cmpRatio:", calc)
    return calc

from operator import itemgetter

def sort(wl, comparator):
    """
    Sorts the list of subjects' names in descending order
    acording to the comparator.
    """

    print(len(wl))
    sl = []
    rl = []

    if len(wl) == 1 or len(wl) == 0:
        return l

    if len(wl) == 2:
        if comparator(wl[0][1], wl[1][1]):
            results = [wl[0], wl[1]]
        else:
            results = [wl[1], wl[0]]
        return results

    high = len(rl)
    low = 0
    # x = (high + low) / 2

    # handle x == 0 case
    x = (high + low) / 2
    loop_num = 0
    # The code needs to stop using list data and actually pull data from list and stuff
    while wl or sl:
        ##### Scaffold
        print("AIM: Move all items from wl to rl, sorted, in logn time")
        print("ACTION: Loop until wl is empty")
        print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                x, high, low, wl, sl, rl, loop_num))
        print("ACTION IMPLEMENTING...")
        raw_input()
        ##### Actual Code
        if wl and len(sl) == 0: # Only pop from full list, but only when len(sl) == 0
            ##### Scaffold
            print("AIM: If wl has items, and sl doesn't, give an item to sl for rl transfer")
            print("ACTION: ^^^^")
            print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            print("ACTION IMPLEMENTING...")
            raw_input()
            ##### Actual Code
            sl = [wl.pop()]
            ##### Scaffold
            print("ACTION COMPLETE.\n")
            print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            raw_input()
            ##### End Scaffold

        if len(rl) == 0 and sl: # If there's nothing in rl, just pop sl into it.
            ##### Scaffold
            print("AIM: If rl is empty, simply move item from sl to rl")
            print("ACTION: ^^^^")
            print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            print("ACTION IMPLEMENTING...")
            raw_input()
            ##### Actual Code
            rl = [sl.pop()]
            high = len(rl)
            low = 0
            loop_num += 1
            ##### Scaffold
            print("ACTION COMPLETE.\n")
            print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            raw_input()
            ##### End Scaffold
            continue
        # if len(rl) == 1 and sl...
            # Needs to restart

        if x == 0:
            ##### Scaffold
            print("AIM: If x is at 0, simply compare sl with 1st value of rl, \
                then put it at [0:0] if True or [1:1] if not")
            print("ACTION: ^^^^")
            print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            print("ACTION IMPLEMENTING...")
            raw_input()
            ##### Actual Code
            if comparator(sl[0][1], rl[0][1]):
                rl.insert(x, sl.pop()) # Can I do the sl without the index?
            else:
                rl.insert(x+1, sl.pop())
            high = len(rl)
            low = 0
            ##### Scaffold
            print("ACTION COMPLETE.\n")
            print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            raw_input()
            ##### End Scaffold

        # elif len(rl) == 2:
        #     ##### Scaffold
        #     print("AIM: Prevent incorrect sorting from the x == len(rl) -1 conditional by handling the len(rl) == 2" \
        #         "scenario.")
        #     print("ACTION: Check if it's ")
        #     print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
        #             x, high, low, wl, sl, rl, loop_num))
        #     print("ACTION IMPLEMENTING...")
        #     raw_input()
        #     ##### Actual Code
        #     if comparator(sl[0][1], rl[0][1]):
        #         rl.insert(x, sl.pop()) # Can I do the sl without the index?
        #     else:
        #         rl.insert(x+1, sl.pop())
        #     high = len(rl)
        #     low = 0
        #     ##### Scaffold
        #     print("ACTION COMPLETE.\n")
        #     print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
        #             x, high, low, wl, sl, rl, loop_num))
        #     raw_input()
        #     ##### End Scaffold

        elif x == len(rl) - 1 and len(rl) > 2:
            ##### Scaffold
            print("\nAIM: If x is equal to the length of the list or just before it, \
                either append it, or put it just before the end value")
            print("ACTION: ^^^^")
            print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            print("ACTION IMPLEMENTING...")
            raw_input()
            ##### Actual Code
            if comparator(sl[0][1], rl[x][1]):
                rl.insert(x, sl.pop())
            else:
                rl.insert(x+1, sl.pop())
            high = len(rl)
            low = 0
            ##### Scaffold
            print("ACTION COMPLETE.\n")
            print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            raw_input()
            ##### End Scaffold
        else:
            ##### Scaffold
            print("\nAIM: Do actual bisection sort here.")
            print("ACTION: Sort by the 4 conditions... TT, TF, FT, FF")
            print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            print("ACTION IMPLEMENTING...")
            raw_input()
            ##### Actual Code
            if comparator(sl[0][1], rl[x-1][1]) and comparator(sl[0][1], rl[x][1]):
                ##### Scaffold
                print("\nAIM: If it's larger than both items, cut the half of the search space.\
                    after x away.")
                print("ACTION: Set lower to x")
                print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                print("ACTION IMPLEMENTING...")
                raw_input()
                ##### Actual Code
                high = x
                ##### Scaffold
                print("ACTION COMPLETE.\n")
                print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                raw_input()
                ##### End Scaffold

            elif comparator(sl[0][1], rl[x-1][1]) and  comparator(sl[0][1], rl[x][1]) == False:
                print("\nAIM: If it's larger than the one above and lower than the one below, stop the program \
                    because it's not sorting correctly" )
                print("ACTION: Set lower to x")
                print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                print("ACTION IMPLEMENTING...")
                raw_input()
                ##### Actual Code
                print("Program not sorting correctly. Exiting...")
                import sys
                sys.exit()
                ##### Scaffold
                print("ACTION COMPLETE.\n")
                print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                raw_input()
                ##### End Scaffold
            elif comparator(sl[0][1], rl[x-1][1]) == False and  comparator(sl[0][1], rl[x][1]):
                print("\nAIM: If less than the one above but greater than the one below, put sl between the two.")
                print("ACTION: Pop sl into rl[x:x]. Reset high and low to len(rl) and 0")
                print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                print("ACTION IMPLEMENTING...")
                raw_input()
                ##### Actual Code
                rl.insert(x, sl.pop())
                high = len(rl)
                low = 0
                ##### Scaffold
                print("ACTION COMPLETE.\n")
                print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                raw_input()
                ##### End Scaffold
            elif comparator(sl[0][1], rl[x-1][1]) == False and  comparator(sl[0][1], rl[x][1]) == False:
                ##### Scaffold
                print("\nAIM: If sl == to either the one above or below it, slap sl in the middle. Else cut the \
                    search space before x away.")
                print("ACTION: Check x_above and x_below for equivalency. If so, set rl[x:x] to sl. If not, set \
                    upper to x. ")
                print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                print("ACTION IMPLEMENTING...")
                raw_input()
                ##### Actual Code
                if comparator.__name__ == "cmpValue":
                    pass
                elif comparator.__name__ == "cmpWork":
                    pass
                elif comparator.__name__ == "cmpRatio":
                    print("\nAIM: If the function name is cmpRatio, check for equal value/work ratios, to determine\
                        whether to plop x down now, or cut the upper half of the search space away." )
                    print("ACTION: Calculate and remember the ratios for each and check for equivalency between sl and \
                        the two rl values. If so, plop x in the middle (for now, until a secondary sort becomes available. \
                        Reset upper and lower. Else, cut search space above x away.)")
                    print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                            x, high, low, wl, sl, rl, loop_num))
                    print("ACTION IMPLEMENTING...")
                    raw_input()
                    ##### Actual Code
                    calc_sl = float(sl[0][1][VALUE])/sl[0][1][WORK]
                    calc_rl_up = float(rl[x-1][1][VALUE])/rl[x-1][1][WORK]
                    calc_rl_below = float(rl[x][1][VALUE])/rl[x][1][WORK]
                    if calc_sl == calc_rl_up or calc_sl == calc_rl_below:
                        raw_input()
                        rl.insert(x, sl.pop())
                        high = len(rl)
                        low = 0
                    else:
                        low = x
                    ##### Scaffold
                    print("ACTION COMPLETE.\n")
                    print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                            x, high, low, wl, sl, rl, loop_num))
                    raw_input()
                    ##### End Scaffold


                ##### Scaffold
                print("ACTION COMPLETE.\n")
                print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                        x, high, low, wl, sl, rl, loop_num))
                raw_input()
                ##### End Scaffold
            ##### Scaffold
            print("ACTION COMPLETE.\n")
            print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                    x, high, low, wl, sl, rl, loop_num))
            raw_input()
            ##### End Scaffold

        x = (high + low) / 2
        loop_num += 1
        ##### Scaffold
        print("ACTION COMPLETE.\n")
        print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
                x, high, low, wl, sl, rl, loop_num))
        raw_input()


        ##### End Scaffold
    return rl
    # print("x, x_above, x_below", x, x_above, x_below)
    # print("sl, rl", sl, rl)
    # Make sure it selects the item above x

    # while len(l) > 0:
    #
    #     if comparator


sort(wl=loadSubjects(SUBJECT_FILENAME).items(), comparator=cmpRatio)
# ordered_subjects = sort(wl=loadSubjects(SUBJECT_FILENAME).items(), comparator=cmpRatio)
# print(["{}\n".format(x) for x in ordered_subjects])

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    # subjectsCopy = sorted(subjects.items(), key=comparator, reverse=True)

    def sort(l, comparator, high=1, low=0):
        """
        Sorts the list of subjects' names in descending order
        acording to the comparator.
        """
        if len(l) == 1 or len(l) == 0:
            return l

        # Create an empty list and add the first item from l into it
        results = [l.pop()]

        # Remember x as upper/lower
        def get_half(upper, lower):
            return int(upper + lower / 2)

        # For each subject in l
        for subject in l: # or while len(l) == 0 and len(results) == start_l
            # Do bisection search within the new list, comparing it to the item
            # above and below a certain point at each search phase

            # Do bisection search until a certain point
            # Remember upper limit as the length of the list
            upper = len(results)
            # Remember lower limit as 0
            lower = 0

            start_list_size = len(l)

            x = get_half(upper, lower)

            # If there's only one thing in the list, compare it to l[0] (which
            # equals l[-1] and put it above or below, and remove it from the original list
            # if len(results) == 0 or x == len(results):
            #     if comparator(l[-1][1], results[-1][1]):
            #         results[-1:-1][1] = [l.pop()]
            #     else:
            #         results.append([l.pop()])
            # # Else
            # # ctr = 0
            # print("len(l)", len(l))
            # while len(l) > 0: # and ctr < 100:
            #
            #     updated_dict = {"l":l, "len(l)":len(l), "results": results, "x":x, "results[x-1:x]":results[x-1:x], "results[x:x+1]":results[x:x+1]}
            #     for each in updated_dict.keys():
            #         print(each + ":" + " " + str(updated_dict[each]) + "\n")
            #
            #         # pass
            #     raw_input("\nPress any key to continue\n\n")
            #
            #     if len(results) == 1:  # and len(results) > 0
            #         if comparator(l[-1][1], results[0][1]):
            #             results[0:0] = [l.pop()]
            #         else: results[1:1] = [l.pop()]
            #         upper = len(results)
            #     # elif len(results) == 2:b
            #         # if comparator(l[-1][1], results[0][1])
            #     else:
            #
            #         # print("results, x, upper, lower, x_above, x_below", results, x, upper, lower, results[x-1:x], results[x:x+1])
            #         try:
            #             x_above = results[x:x+1][1]
            #         except IndexError:
            #             x_above = results[-1][1]
            #         try:
            #             x_below = results[x-1:x][1]
            #         except IndexError:
            #             x_below = results[0]
            #         # print("l[-1], x_above:", l[-1], x_above)
            #         comp_x_above = comparator(l[-1][1], x_above)
            #         comp_x_below = comparator(l[-1][1], x_below)
            #
            #         updated_dict2 = {"x":x, "x_above":x_above, "x_below":x_below, "comp_x_above":comp_x_above, "comp_x_below":comp_x_below, "upper":upper, "lower":lower}
            #         for each in updated_dict2.keys():
            #             print(each + ":" + " " + str(updated_dict2[each]) + "\n")
            #         raw_input("Press any key to continue")
            #
            #         # comp(x-above) can't be true while comp(x-below) is false
            #
            #         # assert that x-above > x-below
            #         # comp(x-above) can't be true while comp(x-below) is false
            #         # print("x_above, x_below:", x_above, x_below)
            #         print("x_above, x_below:", x_above, x_below)
            #         assert comparator(x_above, x_below), "x_above, x_below: {}, {}".format(x_above, x_below)
            #         # if comp(x-above) is true and comp(x-below) is true,
            #         if comp_x_above and comp_x_below:
            #             # split the search area to upper half of remaining area
            #             lower = x
            #         # if comp(x-above) is false and comp(x-below) is true,
            #         elif comp_x_above == False and comp_x_below:
            #             # add current subject to new list at x:x and remove it
            #             results[x:x] = l.pop()
            #             # from the old list
            #             # Consider using recursion for this...
            #         # if comp(x-above) is false and comp(x-below) is false,
            #         elif comp_x_above == False and comp_x_below == False:
            #             # if x == x-above or x== x-below,
            #             if l[-1] == x_above or l[-1] == x_below:
            #                 # Advanced-ish route
            #                     # (Go through all element in the list near x that are
            #                     # equal to x, and secondary sort them using this
            #                     # exact same process, and when done, take that secon-
            #                     # dary list, insert it at x:x, and remove x from old
            #                     # list )
            #                 # add current subject to new list at x:x and remove it
            #                 results[x:x] = l.pop()
            #                 # from the old list
            #                 # Consider using recursion for this...
            #             # else:
            #             else:
            #                 # split the search area to lower half of remaining area
            #                 upper = x
            #                 # Run this again
            #
            #     x = get_half(upper, lower)

                # ctr += 1
            # assert ctr < 90, "Terminated an infinite loop."
        return results
            # def test_sort(sort):
            #     master_one = [1, 2, 3]
            #     test_zero = [3]
            #     test_end = [1, 2, 3, 4, 5, 6]
            #     assert sort()

    def test_sorted():
        """
        How I* know sorted works:

        1. A single subject list simply returns the list
        2. Everything is in the correct order, no number for a specific value
           is less than the one after it
            - Should equal a normal sort, with the tuples normalized.
        3. Should return a list of KEYS in order
        (Should sort from least work to most work... sort by density)

        """
        small_list = loadSubjects(SHORT_SUBJECT_FILENAME).items()[0:5]
        sorted_list = [('6.00', (10, 1)), ('6.10', (8, 18)), ('6.19', (8, 19)), ('6.09', (3, 7)), ('6.08', (1, 10))]
        sorted_list_2 = [('6.09', (3, 7)), ('6.08', (1, 10))]

        assert sort([small_list[0]], cmpValue) == [loadSubjects(SHORT_SUBJECT_FILENAME).items()[0]], "Single item list should return the list as is. " \
                                                                                                    "Sort value: {}".format(sort([small_list[0]], cmpValue)) + \
                                                                                                    "\nExpected Value: {}".format([loadSubjects(SHORT_SUBJECT_FILENAME).items()[0]])
        print("Test 1 passed")
        assert sort([], cmpValue) == []
        print("Test 2 passed")
        print("sort(small_list, cmpValue), sorted_list:", sort(small_list, cmpValue), sorted_list)
        assert sort(small_list, cmpValue) == sorted_list, "sort(small_list, cmpValue), sorted_list: {}".format(sort(small_list, cmpValue), sorted_list)
        print("Test 3 passed")
        assert sort(small_list[0:2], cmpValue) == sorted_list_2
        print("Test 4 passed")

        #     print("Tests completed")
        # except AssertionError:
        #     print(sort([small_list[0]], cmpValue))



        # If at one, and True, True, just set it to [0:0]

    test_sorted()
    sorted_results = sort(l=subjects, comparator=comparator)
    totalVal = 0
    totalWork = 0
    i = 0

    # This is another
    # while totalWork < maxWork and i < len(sorted_reduced_dict):
    #     # if both can fit, just add it,
    #
    #     # if it can't fit, try switching each of the current items with another,
    #     # keep whichever increases the item by the most
    #     if (totalWork + subjectsCopy[i][1]) <= maxWork:
    #         results[subjectsCopy[i][0]] = subjectsCopy[i][1]
    #         totalVal += subjectsCopy[i][1]
    #         totalWork += subjectsCopy[i][2]
    #         i += 1
    #     else:
    #         # If prospect > least optimal and if switched < maxWeight, make it happen
    #         # How to find the least optimal using a dictionary and not a simple list, though
    #         least_optimal =
    #         for each in results
    #         if comparator(subjectsCopy[i][1], )
    #         # I think this is brute force... keep this down...
    #         # Compare each subject I* have with the current prospect
    #         # If the subject provides a better optimization value:
    #             # Test that switching the prospect with the current subject
    #             # will not exceed the weight limit
    #             # If it does exceed, skip this current subject--continue Comparing
    #             # current prospect with the next subject, and run this test against
    #             # If it does not exceed the weight limit, replace the current
    #             # subject with the current prospect and vice versa, and recalculate totatWork and
    #             # totalValue
    #                 # continue comparing the new current prospect with the remaining
    #                 # current subjects
    #         current_prospect = subjectsCopy[i][1]
    #         for each in results:
    #             if comparator(current_prospect, each[1]):
    #                 totalValCopy = totalVal
    #                 totalWorkCopy = totalWork
    #                 if totalWorkCopy - each[1] + subjectsCopy[i][1] <
    #                 test_list = results.copy()
    #                 test_list.remove(each)
    #                 test_list.append(subjectsCopy[i][1])
    #                 if test_list[1]
    #
    #
    # # This is another...
    # # while totalWork < maxWork and i < len(sorted_reduced_dict):
    # #     if (totalWork + sorted_reduced_dict[i][2]) <= maxWork:
    # #         results[sorted_reduced_dict[i][0]] = sorted_reduced_dict[i][1:2]
    # #         totalVal += sorted_reduced_dict[i][1]
    # #         totalWork += sorted_reduced_dict[i][2]
    # #         i += 1
    #
    #
    # # This is one way of doing it...
    #
    # # Reduce the dictionary items list into basic tuples,
    # reduced_dict = [(x[0],x[1][0], x[1][1]) for x in loadSubjects(SHORT_SUBJECT_FILENAME).items()]
    # # sort them that way,
    # sorted_reduced_dict = sorted(reduced_dict, key=itemgetter(2), reverse=True)
    # # do the greedy search,
    # while totalWork < maxWork and i < len(sorted_reduced_dict):
    #     if (totalWork + sorted_reduced_dict[2]) <= maxWork:
    #         results[sorted_reduced_dict[0]] = sorted_reduced_dict[1:2]
    #         totalVal += sorted_reduced_dict[1]
    #         totalWork += sorted_reduced_dict[2]
    #         i += 1
    #
    # return results

# print(isinstance(sorted(loadSubjects(SHORT_SUBJECT_FILENAME).items(), key=itemgetter(1), reverse=True), list))
#print(greedyAdvisor(loadSubjects(SHORT_SUBJECT_FILENAME), maxWork = 20, ))
    # then return the 1st element of the tuple as the key,
    # the remaining as the value.


    # Organizing a list of integers from greatest to least
    # Selecting a specific element of a tuple

    # Combine the key with the values in as  tuple
    # while totalWork < maxWork and i < len(Items)):
    #     if (totalWork + subjectsCopy[i])
# reduced_dict = [(x[0],x[1][0], x[1][1]) for x in loadSubjects(SHORT_SUBJECT_FILENAME).items()]
# print(reduced_dict)
# print(sorted(reduced_dict, key=itemgetter(2), reverse=True))
#print(loadSubjects(SHORT_SUBJECT_FILENAME).items())
# print(sorted(loadSubjects(SHORT_SUBJECT_FILENAME).items(), key=operator.itemgetter(1,1), reverse=True))
# Unknown problems with unknown solutions
# Organizing a dictionary list with tuples as values by a specific index of each tuple
# Properly implementing a Greedy Search
# Known problems with known solutions
# Organizing a list of integers from greatest to least
# Selecting a specific element of a tuple
# Executing a while loop with a deprecating function
# Bisection Search
# Comparing one item against another

# greedyAdvisor(subjects=[], maxWork=15, comparator=cmpValue)

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
