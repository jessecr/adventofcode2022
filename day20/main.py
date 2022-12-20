def runit(nums, iterations):
    num_nums = len(nums)
    idxs = list(range(num_nums))
    for _ in range(iterations):
        for i in range(num_nums):
            idx = idxs.index(i)
            v = nums[idx]
            if v == 0:
                continue
            dest = (idx + v) % (num_nums - 1)
            nums.pop(idx)
            nums[dest:dest] = [v]
            idxs.pop(idx)
            idxs[dest:dest] = [i]

    zero_idx = nums.index(0)
    n1 = nums[(zero_idx + 1000) % num_nums]
    n2 = nums[(zero_idx + 2000) % num_nums]
    n3 = nums[(zero_idx + 3000) % num_nums]

    return sum([n1, n2, n3])


with open('input.txt', 'r') as fd:
    nums = list(map(int, fd.read().splitlines()))

print('Part 1:', runit(nums[:], 1))
print('Part 2:', runit([n * 811589153 for n in nums], 10))
