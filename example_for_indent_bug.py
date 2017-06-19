# Example for indent Building

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
    subjectsCopy = sorted(subjects.items(), key=comparator, reverse=True)
    results = dict()
    totalVal = 0
    totalWork = 0
    i = 0

    def sort(l, comparator, high=1, low=0):
        """
        Sorts the list of subjects' names in descending order
        acording to the comparator.
        """

        # Create an empty list and add the first item from l into it
        results = [l.pop()]
        # Remember upper limit as the length of the list
        upper = len(l)
        # Remember lower limit as 0
        lower = 0
        # Remember x as upper/lower
        def get_half(self, upper, lower):
            return int(upper + lower) / 2
        x = get_half(upper/lower)

        # For each subject in l
        for subject in l: # or while len(l) == 0 and len(results) == start_l
            # Do bisection search within the new list, comparing it to the item
            # above and below a certain point at each search phase

            # Do bisection search until a certain point
            start_list_size = len(l)

            # while len(l) == start_list_size:

            # If there's only one thing in the list, compare it to l[0] (which
            # equals l[-1] and put it above or below, and remove it from the original list
            if len(results) == 0 or x == len(results):
                if comparator(l[-1], results[-1]):
                    results[-1:-1] = [l.pop()]
                else:
                    results.append([l.pop()])
            # Else:
            elif x == 0:  # and len(results) > 0
                if comparator(l[-1], results[0]):
                    results[0:0] = [l.pop()]
                else results[1:1] = [l.pop()]
            else:
                x_above = results[x-1:x]
                x_below = results[x:x+1]
                comp_x_above = comparator(x, x_above)
                comp_x_below = comparator(x, x_below)
                # comp(x-above) can't be true while comp(x-below) is false

                # assert that x-above > x-below
                # comp(x-above) can't be true while comp(x-below) is false
                assert comparator(x_above, x_below)
                # if comp(x-above) is true and comp(x-below) is true,
                if comp_x_above and comp_x_below:
                    # split the search area to upper half of remaining area
                    lower = x
                # if comp(x-above) is false and comp(x-below) is true,
                elif comp_x_above == False and comp_x_below:
                    # add current subject to new list at x:x and remove it
                    results[x:x] = l.pop()
                    # from the old list
                    # Consider using recursion for this...
                # if comp(x-above) is false and comp(x-below) is false,
                elif comp_x_above == False and comp_x_below == False:
                    # if x == x-above or x== x-below,
                    if x == x_above or x = x_below:
                        # Advanced-ish route
                            # (Go through all element in the list near x that are
                            # equal to x, and secondary sort them using this
                            # exact same process, and when done, take that secon-
                            # dary list, insert it at x:x, and remove x from old
                            # list )
                        # add current subject to new list at x:x and remove it
                        results[x:x] = l.pop()
                        # from the old list
                        # Consider using recursion for this...
                    # else:
                else:
                        # split the search area to lower half of remaining area
                        # Run this again
