import streamlit as st
def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
def main():
    st.title("Find the largest among the 3 given numbers")
    st.write("Enter three numbers below:")

    num1 = st.number_input("Number 1", value=0, step=1)
    num2 = st.number_input("Number 2", value=0, step=1)
    num3 = st.number_input("Number 3", value=0, step=1)

    if st.button("Find the largest number"):
        largest_num = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is {largest_num}")

if __name__ == "__main__":
    main()