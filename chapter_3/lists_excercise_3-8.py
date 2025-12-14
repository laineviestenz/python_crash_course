bucket_list = ["colorado", "nyc", "massachusetss", "nepal", "greenland"]

#temporarily change list order
print(bucket_list)
print(sorted(bucket_list))
print(sorted(bucket_list, reverse = True))
print(bucket_list)

#Begin permanent changes to the list order
bucket_list.reverse()
print (bucket_list)

#reverse the permanent change
bucket_list.reverse()
print (bucket_list)

#permanently sort
bucket_list.sort()
print(bucket_list)

#permanently sort in reverse
bucket_list.sort(reverse = True)
print(bucket_list)