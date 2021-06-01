def action_counter():
    counter = 0

    def count_valid(counter):
        resoult = counter
        counter += 1
        return resoult

    return count_valid
