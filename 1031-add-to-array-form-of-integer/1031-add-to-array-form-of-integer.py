class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
            new_list = []
            carry = k
            i = len(num) - 1

            while i >= 0 or carry > 0:
                if i >= 0:
                    carry += num[i]
                new_list.append(carry % 10)
                carry //= 10
                i -= 1

            new_list.reverse()
            return new_list
