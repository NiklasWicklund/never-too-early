# Rules used in the study with some having an additional description.

### Rules from PMD

| Name                       | Category        | Description                                                                                                     |
| --------------------------| ---------------| ----------------------------------------------------------------------------------------------------------------|
| SystemPrintln              | Best Practices | Avoid using System.out.print or System.err.print and instead use a logger.                                     |
| UnusedAssignment           | Best Practices | Avoid assignments to variables that are never used.                                                             |
| UnusedLocalVariable        | Best Practices | Local variables should not be declared and never used.                                                         |
| UnusedPrivateField         | Best Practices | Private fields should not be declared or assigned and never used.                                              |
| UnusedPrivateMethod        | Best Practices | Detects if private methods are declared and never used.                                                         |
| UseCollectionIsEmpty       | Best Practices | .isEmpty() should be used instead of .size() == 0.                                                               |
| UnusedImports              | Best Practices | Detects import statements that are never used or duplicate imports.                                             |
| MissingOverride            | Best Practices | "Annotating overridden methods with @Override ensures at compile time that the method really overrides one, which helps refactoring and clarifies intent." |
| OneDeclarationPerLine      | Best Practices | ~                                                                                                                |
| CommentRequired            | Code Style     | Detects improper usage of Java Documentation, this study does not require JavaDocs for field variables.          |
| UselessParentheses         | Code Style     | ~                                                                                                                |
| FormalParameterNamingConventions | Code Style | ~                                                                                                                |
| MethodNamingConventions     | Code Style     | ~                                                                                                                |
| LocalParameterNamingConventions | Code Style  | ~                                                                                                                |
| UseDiamondOperatior        | Code Style     | ~                                                                                                                |
| CognitiveComplexity        | Design         | ~                                                                                                                |
| ExcessiveMethodLength      | Design         | ~                                                                                                                |
| NcssCount                  | Design         | Non-Commenting Source Statements, detects if the number of lines in methods and classes exceed the set amount (60 for methods and 1500 for classes). |
| AvoidDeeplyNestedIfStmts   | Design         | ~                                                                                                                |
| AvoidThrowingNullPointerException | Design   | ~                                                                                                                |
| AvoidCatchingGenericException | Design      | ~                                                                                                                |
| LogicInversion             | Design         | ~                                                                                                                |
| SimplifyBooleanExpressions | Design         | ~                                                                                                                |
| SimplifyBooleanReturns     | Design         | ~                                                                                                                |
| SingularField              | Design         | Detects field variables that are used in a single method that instead could be local variables.                  |
| UncommentedEmptyMethodBody | Documentation  | ~                                                                                                                |
| AvoidCatchingNPE           | Error Prone    | ~                                                                                                                |
| CompareObjectsWithEquals   | Error Prone    | ~                                                                                                                |
| EmptyCatchBlock            | Error Prone    | ~                                                                                                                |
| EmptyIfStmt                | Error Prone    | ~                                                                                                                |
| EmptyStatementNotInLoop    | Error Prone    | ~                                                                                                                |
| EmptyStatementBlock        | Error Prone    | ~                                                                                                                |
| UnconditionalIfStatement  | Error Prone    | ~                                                                                                                |

### Rules from SonarSource

| Name                                 | Category    | Description                                                                                                               |
|--------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------|
| ConditionalUnreachableCode           | Bug         | ~                                                                                                                         |
| LoopExecutingAtMostOnce              | Bug         | ~                                                                                                                         |
| CommentedOutCodeLine                 | Code Smell  | Detects commented out code.                                                                                                |
| WildcardImportsShouldNotBeUsed       | Code Smell  | ~                                                                                                                         |
| IfElseIfStatementEndsWithElse        | Code Smell  | ~                                                                                                                         |
| MissingCurlyBraces                   | Code Smell  | ~                                                                                                                         |
| TooManyStatementsPerLine             | Code Smell  | ~                                                                                                                         |
| IdenticalCasesInSwitch               | Code Smell  | ~                                                                                                                         |
| MagicNumber                          | Code Smell  | Detects the use of literals instead of assigning them to variables.                                                        |
| ConditionalOnNewLine                 | Code Smell  | Conditionals should start on new lines.                                                                                    |
| DanglingElseStatements               | Code Smell  | ~                                                                                                                         |
| MethodIdenticalImplementations       | Code Smell  | ~                                                                                                                         |

