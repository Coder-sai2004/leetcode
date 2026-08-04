class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Stores the frequency of digits for every row
        row_maps = []

        # Stores the frequency of digits for every column
        column_maps = []

        # Stores the frequency of digits for every 3x3 sub-box
        box_maps = []

        # Build frequency tables for all rows and columns
        for row_index in range(len(board)):
            row_frequency = {}
            column_frequency = {}

            for col_index in range(len(board[0])):
                # Count occurrences of digits in the current row
                if board[row_index][col_index] != '.':
                    row_frequency[board[row_index][col_index]] = (
                        row_frequency.get(board[row_index][col_index], 0) + 1
                    )

                # Count occurrences of digits in the current column
                if board[col_index][row_index] != '.':
                    column_frequency[board[col_index][row_index]] = (
                        column_frequency.get(board[col_index][row_index], 0) + 1
                    )

            row_maps.append(row_frequency)
            column_maps.append(column_frequency)

        # Initial boundaries for traversing each 3x3 box
        box_row_start = 0
        box_col_start = 0
        box_row_end = 3
        box_col_end = 3

        # Build frequency tables for all 3x3 boxes
        for box_index in range(len(board)):
            if box_index != 0:
                # Move to the next row of boxes after every third box
                if box_index % 3 == 0:
                    box_row_start += 3
                    box_row_end += 3
                    box_col_start = 0
                    box_col_end = 3
                # Otherwise move to the next box in the same row
                else:
                    box_col_start += 3
                    box_col_end += 3

            box_frequency = {}

            # Count occurrences of digits inside the current 3x3 box
            for row in range(box_row_start, box_row_end):
                for col in range(box_col_start, box_col_end):
                    if board[row][col] != '.':
                        box_frequency[board[row][col]] = (
                            box_frequency.get(board[row][col], 0) + 1
                        )

            box_maps.append(box_frequency)

        # Reset box boundaries for validation
        check_row_start = 0
        check_col_start = 0
        check_row_end = 3
        check_col_end = 3

        # Validate every cell using the precomputed frequency tables
        for box_index in range(len(board)):
            if box_index != 0:
                # Move to the corresponding 3x3 box
                if box_index % 3 == 0:
                    check_row_start += 3
                    check_row_end += 3
                    check_col_start = 0
                    check_col_end = 3
                else:
                    check_col_start += 3
                    check_col_end += 3

            for row in range(check_row_start, check_row_end):
                for col in range(check_col_start, check_col_end):
                    if board[row][col] != '.':
                        # Retrieve frequency maps for the current row, column, and box
                        row_frequency = row_maps[row]
                        column_frequency = column_maps[col]
                        box_frequency = box_maps[box_index]

                        # If a digit appears more than once in any row, column, or box,
                        # the Sudoku board is invalid
                        if (
                            row_frequency[board[row][col]] > 1
                            or column_frequency[board[row][col]] > 1
                            or box_frequency[board[row][col]] > 1
                        ):
                            return False

        return True