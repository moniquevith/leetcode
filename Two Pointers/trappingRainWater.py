def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    pointer1 = 0
    pointer2 = pointer1 + 1
    while (pointer1 <= pointer2):
        if height[pointer2] >= height[pointer1] and pointer2 != pointer1 + 1: # check for next largest height and pointer2 is not next to pointer1
            h = min(height[pointer1], height[pointer2]):
            w = pointer2 - pointer1 - 1
            blocks_inbetween = 0
            for idx in range(pointer1, pointer2, 1):
                if idx == pointer1 or idx == pointer2:
                    continue
                blocks_inbetween += height[idx]
            v = h * w - blocks_inbetween
        pointer1 = pointer2
        pointer2 = pointer1 + 1

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# expected output = 6
trap(height)