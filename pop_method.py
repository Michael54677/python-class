### Using the pop() method

subscribers = ['michael@example.com', 'id@example.com', 'school@example.com']
print(subscribers)

#poping a subcribers from a list
popped_subscribers = subscribers.pop()
print(subscribers)
print(popped_subscribers)

#using the pop() method to show the first/second/third subcriber on the list 
subscribers = ['michael@example.com', 'id@example.com', 'school@example.com']
first_subscriber = subscribers.pop(0)
print("Your first subscriber was " + first_subscriber + ".")

second_subscriber = subscribers.pop(1)
print("Your second subscriber was " + second_subscriber + ".")

#Using the remove method
subscribers = ['michael@example.com', 'id@example.com', 'school@example.com']
print(subscribers)

subscribers.remove('id@example.com')
print(subscribers)

subscribers = ['michael@example.com', 'id@example.com', 'school@example.com']
subscribed_by_mistake = 'michael@example.com'
subscribers.remove(subscribed_by_mistake)
print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up. ")