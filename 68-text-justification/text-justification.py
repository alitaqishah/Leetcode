class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            line_words = []
            line_length = 0

            # Words ko greedily line mein add karo
            while i < len(words):
                word = words[i]

                # Minimum required length:
                # word lengths + 1 space before this word
                if line_length + len(word) + len(line_words) > maxWidth:
                    break

                line_words.append(word)
                line_length += len(word)
                i += 1

            # Last line
            if i == len(words):
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                break

            # Sirf ek word hai
            if len(line_words) == 1:
                line = line_words[0]
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Normal fully-justified line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            spaces_each = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]

                spaces = spaces_each

                if j < extra_spaces:
                    spaces += 1

                line += " " * spaces

            line += line_words[-1]

            result.append(line)

        return result