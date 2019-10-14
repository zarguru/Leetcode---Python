class Solution:
    def evaluate(self, expression: str) -> int:
        
        def parse(expre, cur):
            # start = cur
            while expre[cur] == ' ':
                cur += 1 #expre = expre[0:cur] + expre[cur+1:]                
            end = cur + 1
            l = len(expre)
            if expre[cur] == '(':
                count = 1 
                while count > 0:
                    if expre[end] == '(':
                        count += 1
                    elif expre[end] == ')':
                        count -= 1
                    end += 1
            else:
                while end < l and expre[end] != ' ':
                    end += 1
            return expre[cur : end], end #+ 1
        
        def helper(expr, m):
            if not expr:
                return 0#, m
            cur = 0
            while expr[cur] == ' ':
                cur += 1
            if expr[cur] == '-' or expr[cur].isdigit():   # (expr[0] >= '0' and expr[0] <= '9'):
                return int(expr[cur:])    #, m    # m[expr]
            if expr[cur] != '(':
                return m[expr[cur:]][-1]      #, m  # cmd, cur = parse(expr, 0) #int('x' in m), m #
            else:
                s = expr[cur +1 : -1]
                cmd, cur = parse(s, 0)
                if cmd == "let":
                    varset = []
                    while True:
                        var, cur = parse(s, cur)
                        if cur > len(s) - 1:
                            exp = helper(var, m)  #return m[var], m # 
                            for var in varset:
                                m[var].pop()
                                if not m[var]:
                                    del m[var]
                            return exp#, m
                        value, cur = parse(s, cur)
                        #m[var] = int(value)
                        # tmp = m[var][-1]
                        if var not in m:
                            m[var] = []
                        m[var].append(helper(value, m))                        
                        varset.append(var)
                elif cmd == "add":
                    s1, cur = parse(s, cur)
                    a1 = helper(s1, m)
                    s1, cur = parse(s, cur)
                    a2 = helper(s1, m)
                    return a1 + a2#, m
                elif cmd == "mult":
                    s1, cur = parse(s, cur)
                    m1 = helper(s1, m)
                    s1, cur = parse(s, cur)
                    m2 = helper(s1, m)
                    return m1 * m2#, m
                
        # m = {}
        res = helper(expression, {})
        return res
        
                
