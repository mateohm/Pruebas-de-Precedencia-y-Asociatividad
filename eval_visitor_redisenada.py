from ExprRedisenadaParser import ExprRedisenadaParser
from ExprRedisenadaVisitor import ExprRedisenadaVisitor


class EvalVisitorRedisenada(ExprRedisenadaVisitor):

    def visitMulDiv(self, ctx: ExprRedisenadaParser.MulDivContext):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        else:
            return left // right

    def visitOnlyTerm(self, ctx: ExprRedisenadaParser.OnlyTermContext):
        return self.visit(ctx.term())

    def visitAddSubRightRec(self, ctx: ExprRedisenadaParser.AddSubRightRecContext):
        left = self.visit(ctx.factor())
        right = self.visit(ctx.term())
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        else:
            return left - right

    def visitOnlyFactor(self, ctx: ExprRedisenadaParser.OnlyFactorContext):
        return self.visit(ctx.factor())

    def visitFactor(self, ctx: ExprRedisenadaParser.FactorContext):
        if ctx.NUM() is not None:
            return int(ctx.NUM().getText())
        return self.visit(ctx.expr())
