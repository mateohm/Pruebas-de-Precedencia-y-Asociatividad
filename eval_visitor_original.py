from ExprOriginalParser import ExprOriginalParser
from ExprOriginalVisitor import ExprOriginalVisitor


class EvalVisitorOriginal(ExprOriginalVisitor):

    def visitAddSubLeftRec(self, ctx: ExprOriginalParser.AddSubLeftRecContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        else:
            return left - right

    def visitMulDivLeftRec(self, ctx: ExprOriginalParser.MulDivLeftRecContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        else:
            return left // right  # división entera

    def visitParens(self, ctx: ExprOriginalParser.ParensContext):
        return self.visit(ctx.expr())

    def visitNumber(self, ctx: ExprOriginalParser.NumberContext):
        return int(ctx.NUM().getText())
