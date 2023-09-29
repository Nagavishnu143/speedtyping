import time

def typing_test():
    sentence = "The quick brown fox jumps over the lazy dog."  # Change the sentence as needed
    print("Type the following sentence:")
    print(sentence)
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    # Count the number of words in the sentence
    words = sentence.split()
    word_count = len(words)
    
    # Calculate typing speed in WPM
    typing_speed = (word_count / elapsed_time) * 60
    
    print(f"Your typing speed: {typing_speed:.2f} WPM")

if __name__ == "__main__":
    typing_test()
