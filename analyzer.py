import ast

class BugFinder(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_FunctionDef(self, node):
        if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            self.issues.append(f"⚠️ Function '{node.name}' is empty.")
        self.generic_visit(node)

    def visit_Compare(self, node):
        if isinstance(node.ops[0], ast.Eq):
            if isinstance(node.comparators[0], ast.Constant) and node.comparators[0].value is None:
                self.issues.append("⚠️ Use 'is None' instead of '== None'")
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            if var_name.startswith("_"):
                self.issues.append(f"⚠️ Variable '{var_name}' might be unused.")
        self.generic_visit(node)


def analyze_code(code):
    try:
        tree = ast.parse(code)
        analyzer = BugFinder()
        analyzer.visit(tree)
        return analyzer.issues if analyzer.issues else ["✅ No major issues found"]
    except SyntaxError as e:
        return [f"❌ Syntax Error: {e}"]
