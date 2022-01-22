from Tweets import Tweet
import time


def main():
    # Create a list for Tweets
    tweets = list()

    while True:

        print("\nTweet Menu")
        print("--------")
        print("1. Make a Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit\n")
        select_type = input("What would you like to do? ")

        if(select_type == '1'):
            # Ask the user for their name and tweet
            author = input("What is your name? ")

            while True:
                    text = input("What would you like to tweet? ")
                    if len(text) > 140:
                        print("Tweets can only be 140 characters!")
                    else:
                        break

            age = time.time()
            print(author, ", your tweet has been saved.")

            # Create a new Tweet
            new_tweet = Tweet(author, text, age)

            # Append the Tweet to the list
            tweets.append(new_tweet)

        if(select_type == '2'):
            #print out the data
            print("Recent Tweets")
            print("---------")

            if(len(tweets) == 0):
                print("There are no recent tweets.")
            else: # Loop through the list
                for tweet in tweets:
                # Use accessor methods to get each Tweets information
                    author = tweet.get_author()
                    text = tweet.get_text()
                    age = tweet.get_age()

                    if 3600 > age > 60:
                        minutes = age // 60
                        print(author, "-", minutes, "m")
                        print(text)

                        if age > 3600:
                            hours = minutes // 60
                            print(author, "-", hours, "h")
                            print(text)
                    else:
                        # Print the Tweets information
                        print(author, "-", age, "s")
                        print(text)

        if(select_type == '3'):
            number_of_tweets = 0
            #look if the list is empty
            if(len(tweets) == 0):
                print("There are no tweets to search")
            else:
                keyword = input("What would you like to search for? ")
                print("Search Results")
                print("---------")
                for tweet in tweets:
                    # Use accessor methods to get each Tweets information
                    author = tweet.get_author()
                    text = tweet.get_text()
                    age = tweet.get_age()

                    if text.find(keyword) != -1:
                        if 3600 > age > 60:
                            minutes = age // 60
                            print(author, "-", minutes, "m")
                            print(text)
                            number_of_tweets += 1
                            if age > 3600:
                                hours = minutes // 60
                                print(author, "-", hours, "h")
                                print(text)
                                number_of_tweets += 1
                        else:
                            # Print the Tweets information
                            print(author, "-", age, "s")
                            print(text)
                            number_of_tweets += 1

                if number_of_tweets == 0:
                    print("No tweet contained", keyword)
                else:
                    print("\nThere were", number_of_tweets, "tweets that contained", keyword)

        if(select_type == '4'):
            print("Thank you for using the Tweet Manger!")
            break

main()
