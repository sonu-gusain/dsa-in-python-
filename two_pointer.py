
#container with most water 


# brute force approch

def area(height):
   areas = []
   lenth = len(height)
   for i in range(lenth):
      for j in range(i+1,lenth):
         minimum = min(height[i],height[j])
         widht  = j-i
         areas.append(minimum*widht)

   return max(areas)
height = [1,8,6,2,5,4,8,3]
print(area(height))


# two pointer approch 


def maxarea(heights):
   max_water = 0
   left = 0
   right = len(heights)-1
   while left < right:
      minimum = min(heights[left] , heights[right])
      width = right - left
      area = width *minimum
      if area > max_water:
         max_water = area

      if height[right] < height[left]:
         right = right - 1 
      else:
         left = left + 1 

   return max_water
heights = [1,8,6,2,5,4,8,3]
print(maxarea(heights))
