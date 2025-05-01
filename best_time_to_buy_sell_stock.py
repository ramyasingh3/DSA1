def max_profit(prices: list[int]) -> int:
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day,
    find the maximum profit you can achieve by buying on one day and selling on a later day.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit that can be achieved
    """
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]  # Keep track of minimum price seen so far
    max_profit = 0         # Keep track of maximum profit seen so far
    
    for price in prices[1:]:
        # Update max_profit if selling at current price gives better profit
        max_profit = max(max_profit, price - min_price)
        # Update min_price if current price is lower
        min_price = min(min_price, price)
    
    return max_profit

def test_max_profit():
    """Test cases for max profit implementation"""
    test_cases = [
        # Basic cases
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),     # No profit possible
        
        # Edge cases
        ([], 0),                   # Empty array
        ([1], 0),                  # Single price
        ([1, 2], 1),              # Two prices, profit possible
        
        # Special cases
        ([2, 4, 1], 2),           # Buy at 2, sell at 4
        ([3, 2, 6, 5, 0, 3], 4),  # Buy at 2, sell at 6
        ([1, 2, 3, 4, 5], 4),     # Buy at 1, sell at 5
        ([5, 4, 3, 2, 1], 0),     # No profit possible
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        assert result == expected, f"Test failed for prices {prices}. Expected {expected}, got {result}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_max_profit()
    
    # Example usage
    example_prices = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [2, 4, 1],
        [3, 2, 6, 5, 0, 3],
    ]
    
    for prices in example_prices:
        result = max_profit(prices)
        print(f"Input: prices = {prices}")
        print(f"Output: {result}")
        
        # Find the actual buy and sell days for the maximum profit
        if result > 0:
            min_price = min(prices)
            buy_day = prices.index(min_price)
            sell_day = prices.index(min_price + result)
            print(f"Explanation: Buy on day {buy_day + 1} (price = {min_price}) and sell on day {sell_day + 1} (price = {min_price + result})\n")
        else:
            print("Explanation: No profit can be made\n") 