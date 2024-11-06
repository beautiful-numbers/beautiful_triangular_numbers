import math
import time

def is_semiprime(n):
    """
    Determines if a number is a semiprime.
    A semiprime is a product of exactly two distinct prime numbers.
    The number 6 is explicitly excluded as per original logic.
    """
    if n == 6:
        return False
    count = 0
    i = 2
    last_factor = None
    while i * i <= n:
        if n % i == 0:
            count += 1
            if count > 2:
                return False
            n //= i
            if last_factor == i:
                return False
            last_factor = i
        else:
            i += 1
    if n > 1:
        count += 1
        if last_factor == n:
            return False
    return count == 2

def apply_filters(T, n):
    """
    Applies the filtering conditions to determine if T is a beautiful triangular number. 
    These filters are applied primarily to exclude non-beautiful triangular numbers, improving computational efficiency.
    """
    # Since T = n(n+1)//2, T is triangular

    if T % n != 0:
        return False, None, None
    median_length = T // n

    if T % 2 != 0 and T % 3 != 0:
        return False, None, None

    if is_semiprime(T):
        return False, None, None

    return True, n, median_length

def analyze_triangle_and_rectangle(T, n, median_length):
    """
    Analyzes the triangle and rectangle based on the given parameters.
    Returns the sections if T is a beautiful triangular number; otherwise, None.
    """
    rows = n + 1
    R = rows * n

    if R != T * 2:
        return None

    first_divisor = 2 if T % 2 == 0 else 3

    if median_length % first_divisor != 0:
        return None
    columns_in_first_section = median_length // first_divisor

    dots_in_first_section = (rows - 1) * columns_in_first_section

    # Generate divisors of T
    divisors = []
    for i in range(1, int(math.isqrt(T)) + 1):
        if T % i == 0:
            divisors.append(i)
            if i != T // i:
                divisors.append(T // i)
    divisors.sort(reverse=True)

    num_pairs = len(divisors) // 2
    paired_divisors = [(divisors[i], divisors[-(i+1)]) for i in range(num_pairs)]

    # Exclude T itself from divisors_before_median
    if num_pairs > 0:
        divisors_before_median = [pair[0] for pair in paired_divisors][1:]  # Exclude T itself
        divisors_after_median = [pair[1] for pair in paired_divisors][1:]   # Exclude 1
    else:
        divisors_before_median = []
        divisors_after_median = []

    if len(divisors_before_median) == 0:
        return None

    # Check if dots_in_first_section matches the first divisor
    if dots_in_first_section != divisors_before_median[0]:
        return None

    sections = []
    sections.append({
        'Columns': columns_in_first_section,
        'Dots': dots_in_first_section
    })

    remaining_columns = median_length - columns_in_first_section

    index = 1  # Start from the second divisor since first was matched in initial section

    while remaining_columns > 1:
        columns_in_next_section = remaining_columns // 2
        if columns_in_next_section == 0:
            break

        dots_in_next_section = (rows - 1) * columns_in_next_section

        if index >= len(divisors_before_median):
            return None

        if dots_in_next_section != divisors_before_median[index]:
            return None

        sections.append({
            'Columns': columns_in_next_section,
            'Dots': dots_in_next_section
        })

        remaining_columns -= columns_in_next_section
        index += 1

    if remaining_columns != 1:
        return None

    last_dots = (rows - 1) * remaining_columns
    if last_dots != n:
        return None

    sections.append({
        'Columns': remaining_columns,
        'Dots': last_dots
    })

    sum_divisors_after_median = sum(divisors_after_median) + 1
    expected_sum = n
    if sum_divisors_after_median != expected_sum:
        return None

    return sections

"""def draw_sigma_triangle(total_dots):
    # Draws a sigma triangle based on the total number of dots.
    # This visual representation helps verify the geometric properties of the triangular number.
"""

def find_beautiful_triangular_numbers(limit_T):
    """
    Finds all beautiful triangular numbers up to limit_T.
    Displays progress updates and visualizations for each beautiful triangular number found.
    """
    beautiful_triangles = []

    total_T_checked = 0
    after_filters = 0
    filtered_numbers = []
    last_reported_percentage = 0

    start_time = time.time()

    limit_n = int((-1 + math.isqrt(1 + 8 * limit_T)) // 2)

    for n in range(1, limit_n + 1):
        T = n * (n + 1) // 2
        if T > limit_T:
            break
        total_T_checked += 1
        passes_filters, n_check, median_length = apply_filters(T, n)
        if not passes_filters:
            # Update progress
            progress_percentage = (n / limit_n) * 100
            if int(progress_percentage) >= last_reported_percentage + 1:  # Update every 1%
                elapsed_time = time.time() - start_time
                print(f"Progress: {int(progress_percentage)}% | Elapsed time: {elapsed_time:.2f}s", end='\r', flush=True)
                last_reported_percentage = int(progress_percentage)
            continue
        after_filters += 1

        sections = analyze_triangle_and_rectangle(T, n_check, median_length)
        if sections is None:
            # Update progress
            progress_percentage = (n / limit_n) * 100
            if int(progress_percentage) >= last_reported_percentage + 1:  # Update every 1%
                elapsed_time = time.time() - start_time
                print(f"Progress: {int(progress_percentage)}% | Elapsed time: {elapsed_time:.2f}s", end='\r', flush=True)
                last_reported_percentage = int(progress_percentage)
            continue

        data = {
            "Triangular Number": T,
            "Side Length (n)": n_check,
            "Median Length": median_length,
            "Sections": sections
        }
        beautiful_triangles.append(data)

        # Update progress
        progress_percentage = (n / limit_n) * 100
        if int(progress_percentage) >= last_reported_percentage + 1:
            elapsed_time = time.time() - start_time
            print(f"Progress: {int(progress_percentage)}% | Elapsed time: {elapsed_time:.2f}s", end='\r', flush=True)
            last_reported_percentage = int(progress_percentage)

    # After loop completes, ensure 100% is printed
    print(f"\nProgress: 100% | Elapsed time: {time.time() - start_time:.2f}s")

    print(f"Total T checked: {total_T_checked}")
    print(f"After applying filters: {after_filters}")
    print(f"Total beautiful triangles found: {len(beautiful_triangles)}\n")

    print("Beautiful Triangular Numbers:")
    for triangle in beautiful_triangles:
        print(f"Triangular Number: {triangle['Beautiful Triangular Number']}, Side Length: {triangle['Side Length (n)']}")
        for idx, section in enumerate(triangle['Sections']):
            print(f"  Section {idx+1}: Columns = {section['Columns']}, Dots = {section['Dots']}")
        print()
    return beautiful_triangles

if __name__ == "__main__":
    # Set the desired limit_T
    limit_T = 34000000  # Adjust as needed, e.g., 1000000 for testing

    # Start the computation
    start_time = time.time()
    beautiful_triangles = find_beautiful_triangular_numbers(limit_T)
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
