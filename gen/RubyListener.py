# Generated from /home/tturek/Documents/personal/UST/Sophomore_2/Compilators/Ruby-2-Python/Project/Ruby.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser

# This class defines a complete listener for a parse tree produced by RubyParser.
class RubyListener(ParseTreeListener):

    # Enter a parse tree produced by RubyParser#prog.
    def enterProg(self, ctx:RubyParser.ProgContext):
        pass

    # Exit a parse tree produced by RubyParser#prog.
    def exitProg(self, ctx:RubyParser.ProgContext):
        pass


    # Enter a parse tree produced by RubyParser#expression_list.
    def enterExpression_list(self, ctx:RubyParser.Expression_listContext):
        pass

    # Exit a parse tree produced by RubyParser#expression_list.
    def exitExpression_list(self, ctx:RubyParser.Expression_listContext):
        pass


    # Enter a parse tree produced by RubyParser#expression.
    def enterExpression(self, ctx:RubyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by RubyParser#expression.
    def exitExpression(self, ctx:RubyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by RubyParser#function_in_call.
    def enterFunction_inline_call(self, ctx:RubyParser.Function_inline_callContext):
        pass

    # Exit a parse tree produced by RubyParser#function_inline_call.
    def exitFunction_inline_call(self, ctx:RubyParser.Function_inline_callContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition.
    def enterFunction_definition(self, ctx:RubyParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition.
    def exitFunction_definition(self, ctx:RubyParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition_body.
    def enterFunction_definition_body(self, ctx:RubyParser.Function_definition_bodyContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition_body.
    def exitFunction_definition_body(self, ctx:RubyParser.Function_definition_bodyContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition_header.
    def enterFunction_definition_header(self, ctx:RubyParser.Function_definition_headerContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition_header.
    def exitFunction_definition_header(self, ctx:RubyParser.Function_definition_headerContext):
        pass


    # Enter a parse tree produced by RubyParser#function_name.
    def enterFunction_name(self, ctx:RubyParser.Function_nameContext):
        pass

    # Exit a parse tree produced by RubyParser#function_name.
    def exitFunction_name(self, ctx:RubyParser.Function_nameContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition_params.
    def enterFunction_definition_params(self, ctx:RubyParser.Function_definition_paramsContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition_params.
    def exitFunction_definition_params(self, ctx:RubyParser.Function_definition_paramsContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition_params_list.
    def enterFunction_definition_params_list(self, ctx:RubyParser.Function_definition_params_listContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition_params_list.
    def exitFunction_definition_params_list(self, ctx:RubyParser.Function_definition_params_listContext):
        pass


    # Enter a parse tree produced by RubyParser#function_definition_param_id.
    def enterFunction_definition_param_id(self, ctx:RubyParser.Function_definition_param_idContext):
        pass

    # Exit a parse tree produced by RubyParser#function_definition_param_id.
    def exitFunction_definition_param_id(self, ctx:RubyParser.Function_definition_param_idContext):
        pass


    # Enter a parse tree produced by RubyParser#return_statement.
    def enterReturn_statement(self, ctx:RubyParser.Return_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#return_statement.
    def exitReturn_statement(self, ctx:RubyParser.Return_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#function_call.
    def enterFunction_call(self, ctx:RubyParser.Function_callContext):
        pass

    # Exit a parse tree produced by RubyParser#function_call.
    def exitFunction_call(self, ctx:RubyParser.Function_callContext):
        pass


    # Enter a parse tree produced by RubyParser#function_call_param_list.
    def enterFunction_call_param_list(self, ctx:RubyParser.Function_call_param_listContext):
        pass

    # Exit a parse tree produced by RubyParser#function_call_param_list.
    def exitFunction_call_param_list(self, ctx:RubyParser.Function_call_param_listContext):
        pass


    # Enter a parse tree produced by RubyParser#function_call_params.
    def enterFunction_call_params(self, ctx:RubyParser.Function_call_paramsContext):
        pass

    # Exit a parse tree produced by RubyParser#function_call_params.
    def exitFunction_call_params(self, ctx:RubyParser.Function_call_paramsContext):
        pass


    # Enter a parse tree produced by RubyParser#function_param.
    def enterFunction_param(self, ctx:RubyParser.Function_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#function_param.
    def exitFunction_param(self, ctx:RubyParser.Function_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#function_unnamed_param.
    def enterFunction_unnamed_param(self, ctx:RubyParser.Function_unnamed_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#function_unnamed_param.
    def exitFunction_unnamed_param(self, ctx:RubyParser.Function_unnamed_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#function_named_param.
    def enterFunction_named_param(self, ctx:RubyParser.Function_named_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#function_named_param.
    def exitFunction_named_param(self, ctx:RubyParser.Function_named_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#function_call_assignment.
    def enterFunction_call_assignment(self, ctx:RubyParser.Function_call_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#function_call_assignment.
    def exitFunction_call_assignment(self, ctx:RubyParser.Function_call_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#all_result.
    def enterAll_result(self, ctx:RubyParser.All_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#all_result.
    def exitAll_result(self, ctx:RubyParser.All_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#elsif_statement.
    def enterElsif_statement(self, ctx:RubyParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#elsif_statement.
    def exitElsif_statement(self, ctx:RubyParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#if_elsif_statement.
    def enterIf_elsif_statement(self, ctx:RubyParser.If_elsif_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#if_elsif_statement.
    def exitIf_elsif_statement(self, ctx:RubyParser.If_elsif_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#if_statement.
    def enterIf_statement(self, ctx:RubyParser.If_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#if_statement.
    def exitIf_statement(self, ctx:RubyParser.If_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#unless_statement.
    def enterUnless_statement(self, ctx:RubyParser.Unless_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#unless_statement.
    def exitUnless_statement(self, ctx:RubyParser.Unless_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#while_statement.
    def enterWhile_statement(self, ctx:RubyParser.While_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#while_statement.
    def exitWhile_statement(self, ctx:RubyParser.While_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#for_statement.
    def enterFor_statement(self, ctx:RubyParser.For_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#for_statement.
    def exitFor_statement(self, ctx:RubyParser.For_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#init_expression.
    def enterInit_expression(self, ctx:RubyParser.Init_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#init_expression.
    def exitInit_expression(self, ctx:RubyParser.Init_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#all_assignment.
    def enterAll_assignment(self, ctx:RubyParser.All_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#all_assignment.
    def exitAll_assignment(self, ctx:RubyParser.All_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#for_init_list.
    def enterFor_init_list(self, ctx:RubyParser.For_init_listContext):
        pass

    # Exit a parse tree produced by RubyParser#for_init_list.
    def exitFor_init_list(self, ctx:RubyParser.For_init_listContext):
        pass


    # Enter a parse tree produced by RubyParser#cond_expression.
    def enterCond_expression(self, ctx:RubyParser.Cond_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#cond_expression.
    def exitCond_expression(self, ctx:RubyParser.Cond_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#loop_expression.
    def enterLoop_expression(self, ctx:RubyParser.Loop_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#loop_expression.
    def exitLoop_expression(self, ctx:RubyParser.Loop_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#for_loop_list.
    def enterFor_loop_list(self, ctx:RubyParser.For_loop_listContext):
        pass

    # Exit a parse tree produced by RubyParser#for_loop_list.
    def exitFor_loop_list(self, ctx:RubyParser.For_loop_listContext):
        pass


    # Enter a parse tree produced by RubyParser#statement_body.
    def enterStatement_body(self, ctx:RubyParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by RubyParser#statement_body.
    def exitStatement_body(self, ctx:RubyParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by RubyParser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:RubyParser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by RubyParser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:RubyParser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by RubyParser#assignment.
    def enterAssignment(self, ctx:RubyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#assignment.
    def exitAssignment(self, ctx:RubyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_assignment.
    def enterDynamic_assignment(self, ctx:RubyParser.Dynamic_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_assignment.
    def exitDynamic_assignment(self, ctx:RubyParser.Dynamic_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#int_assignment.
    def enterInt_assignment(self, ctx:RubyParser.Int_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#int_assignment.
    def exitInt_assignment(self, ctx:RubyParser.Int_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#float_assignment.
    def enterFloat_assignment(self, ctx:RubyParser.Float_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#float_assignment.
    def exitFloat_assignment(self, ctx:RubyParser.Float_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#string_assignment.
    def enterString_assignment(self, ctx:RubyParser.String_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#string_assignment.
    def exitString_assignment(self, ctx:RubyParser.String_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#initial_array_assignment.
    def enterInitial_array_assignment(self, ctx:RubyParser.Initial_array_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#initial_array_assignment.
    def exitInitial_array_assignment(self, ctx:RubyParser.Initial_array_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#array_assignment.
    def enterArray_assignment(self, ctx:RubyParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#array_assignment.
    def exitArray_assignment(self, ctx:RubyParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#array_definition.
    def enterArray_definition(self, ctx:RubyParser.Array_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#array_definition.
    def exitArray_definition(self, ctx:RubyParser.Array_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#array_definition_elements.
    def enterArray_definition_elements(self, ctx:RubyParser.Array_definition_elementsContext):
        pass

    # Exit a parse tree produced by RubyParser#array_definition_elements.
    def exitArray_definition_elements(self, ctx:RubyParser.Array_definition_elementsContext):
        pass


    # Enter a parse tree produced by RubyParser#array_selector.
    def enterArray_selector(self, ctx:RubyParser.Array_selectorContext):
        pass

    # Exit a parse tree produced by RubyParser#array_selector.
    def exitArray_selector(self, ctx:RubyParser.Array_selectorContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_result.
    def enterDynamic_result(self, ctx:RubyParser.Dynamic_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_result.
    def exitDynamic_result(self, ctx:RubyParser.Dynamic_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_.
    def enterDynamic_(self, ctx:RubyParser.Dynamic_Context):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_.
    def exitDynamic_(self, ctx:RubyParser.Dynamic_Context):
        pass


    # Enter a parse tree produced by RubyParser#int_result.
    def enterInt_result(self, ctx:RubyParser.Int_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#int_result.
    def exitInt_result(self, ctx:RubyParser.Int_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#float_result.
    def enterFloat_result(self, ctx:RubyParser.Float_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#float_result.
    def exitFloat_result(self, ctx:RubyParser.Float_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#string_result.
    def enterString_result(self, ctx:RubyParser.String_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#string_result.
    def exitString_result(self, ctx:RubyParser.String_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#comparison_list.
    def enterComparison_list(self, ctx:RubyParser.Comparison_listContext):
        pass

    # Exit a parse tree produced by RubyParser#comparison_list.
    def exitComparison_list(self, ctx:RubyParser.Comparison_listContext):
        pass


    # Enter a parse tree produced by RubyParser#comparison.
    def enterComparison(self, ctx:RubyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RubyParser#comparison.
    def exitComparison(self, ctx:RubyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RubyParser#comp_var.
    def enterComp_var(self, ctx:RubyParser.Comp_varContext):
        pass

    # Exit a parse tree produced by RubyParser#comp_var.
    def exitComp_var(self, ctx:RubyParser.Comp_varContext):
        pass


    # Enter a parse tree produced by RubyParser#lvalue.
    def enterLvalue(self, ctx:RubyParser.LvalueContext):
        pass

    # Exit a parse tree produced by RubyParser#lvalue.
    def exitLvalue(self, ctx:RubyParser.LvalueContext):
        pass


    # Enter a parse tree produced by RubyParser#rvalue.
    def enterRvalue(self, ctx:RubyParser.RvalueContext):
        pass

    # Exit a parse tree produced by RubyParser#rvalue.
    def exitRvalue(self, ctx:RubyParser.RvalueContext):
        pass


    # Enter a parse tree produced by RubyParser#break_expression.
    def enterBreak_expression(self, ctx:RubyParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#break_expression.
    def exitBreak_expression(self, ctx:RubyParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#literal_t.
    def enterLiteral_t(self, ctx:RubyParser.Literal_tContext):
        pass

    # Exit a parse tree produced by RubyParser#literal_t.
    def exitLiteral_t(self, ctx:RubyParser.Literal_tContext):
        pass


    # Enter a parse tree produced by RubyParser#float_t.
    def enterFloat_t(self, ctx:RubyParser.Float_tContext):
        pass

    # Exit a parse tree produced by RubyParser#float_t.
    def exitFloat_t(self, ctx:RubyParser.Float_tContext):
        pass


    # Enter a parse tree produced by RubyParser#int_t.
    def enterInt_t(self, ctx:RubyParser.Int_tContext):
        pass

    # Exit a parse tree produced by RubyParser#int_t.
    def exitInt_t(self, ctx:RubyParser.Int_tContext):
        pass


    # Enter a parse tree produced by RubyParser#bool_t.
    def enterBool_t(self, ctx:RubyParser.Bool_tContext):
        pass

    # Exit a parse tree produced by RubyParser#bool_t.
    def exitBool_t(self, ctx:RubyParser.Bool_tContext):
        pass


    # Enter a parse tree produced by RubyParser#nil_t.
    def enterNil_t(self, ctx:RubyParser.Nil_tContext):
        pass

    # Exit a parse tree produced by RubyParser#nil_t.
    def exitNil_t(self, ctx:RubyParser.Nil_tContext):
        pass


    # Enter a parse tree produced by RubyParser#id_.
    def enterId_(self, ctx:RubyParser.Id_Context):
        pass

    # Exit a parse tree produced by RubyParser#id_.
    def exitId_(self, ctx:RubyParser.Id_Context):
        pass


    # Enter a parse tree produced by RubyParser#terminator.
    def enterTerminator(self, ctx:RubyParser.TerminatorContext):
        pass

    # Exit a parse tree produced by RubyParser#terminator.
    def exitTerminator(self, ctx:RubyParser.TerminatorContext):
        pass


    # Enter a parse tree produced by RubyParser#else_token.
    def enterElse_token(self, ctx:RubyParser.Else_tokenContext):
        pass

    # Exit a parse tree produced by RubyParser#else_token.
    def exitElse_token(self, ctx:RubyParser.Else_tokenContext):
        pass


    # Enter a parse tree produced by RubyParser#crlf.
    def enterCrlf(self, ctx:RubyParser.CrlfContext):
        pass

    # Exit a parse tree produced by RubyParser#crlf.
    def exitCrlf(self, ctx:RubyParser.CrlfContext):
        pass



del RubyParser