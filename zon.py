#!/usr/bin/python
# RETURN AN EMPTY LIST IF NO ITEM ASSOCIATION IS GIVEN
def largestItemAssociation(itemAssociation):
    if len(itemAssociation) == 0:
        return itemAssociation
    largestGroup = itemAssociation[0]
    largestSize = len(itemAssociation[0]) 
    for group in itemAssociation:
        for item in largestGroup:
            if item in group:
                largestGroup = combineGroups(largestGroup,group)

    nextGroup = largestItemAssociation(itemAssociation[1:])
    itemAssociation.append(largestGroup)
    if len(nextGroup) > len(largestGroup):
        return nextGroup
    else:
        return largestGroup
    
def combineGroups(group1,group2):
    allItems = []
    for item in group1: 
        if item not in allItems:
            allItems.append(item)
    for item in group2:
        if item not in allItems:
            allItems.append(item)
    return allItems

#group = [["item","item2"],["item6","item5"],["item3","item4"],["item1","item5"]]
group = [["item1","item2"],["item4","item5"],["item2","item3"],["item5","item6"],["item6","item7"]]
#group = [[],["item1"]]
print largestItemAssociation(group)
