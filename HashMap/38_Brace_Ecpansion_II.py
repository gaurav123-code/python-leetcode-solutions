class Solution(object):
    def braceExpansionII(self, expression):
        def union(a, b):
            return a | b

        def multiply(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)
                    current = multiply(current, part)

                elif expression[i] == ',':
                    result = union(result, current)
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {expression[i]})
                    i += 1

            result = union(result, current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)