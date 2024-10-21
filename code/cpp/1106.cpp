//https://leetcode.com/problems/parsing-a-boolean-expression/
class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> stack;
        for (char ch : expression) {
            if (ch == 't' or ch == 'f' or ch == '!' or ch == '&' or ch == '|')
                stack.push(ch);
            else if (ch == ')') {
                bool hasTrue = false, hasFalse = false;
                char top = stack.top();
                while (top != '!' and top != '&' and top != '|') {
                    stack.pop();
                    if (top == 't')
                        hasTrue = true;
                    else
                        hasFalse = true;
                    top = stack.top();
                }
                stack.pop();
                if (top == '!')
                    stack.push(hasTrue ? 'f' : 't');
                else if (top == '&')
                    stack.push(hasFalse ? 'f' : 't');
                else
                    stack.push(hasTrue ? 't' : 'f');
            }
        }
        return stack.top() == 't';
    }
};
