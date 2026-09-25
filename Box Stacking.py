class Solution:
    def maxHeight(self, height, width, length):
        # Step 1: Generate all rotations of the boxes
        boxes = []
        n = len(height)
        
        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            boxes.append((max(l, w), min(l, w), h))  # l >= w
            boxes.append((max(w, h), min(w, h), l))
            boxes.append((max(l, h), min(l, h), w))
        
        # Step 2: Sort boxes by base area in descending order
        boxes.sort(key=lambda box: box[0] * box[1], reverse=True)
        
        # Step 3: Initialize DP array
        total_boxes = len(boxes)
        dp = [0] * total_boxes
        
        for i in range(total_boxes):
            dp[i] = boxes[i][2]  # Initial height is the height of the box itself
        
        # Step 4: Compute max stack height using DP
        for i in range(total_boxes):
            for j in range(i):
                if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:  # Strictly smaller base
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])
        
        return max(dp)
