import random
from typing import List
import argparse


def _init_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Monty-Hall-Visualizer',
        description="Helps you visualize different setups of the Monty-Hall problem",
        epilog="For questions, please contact symonyshen@gmail.com",
    )
    parser.add_argument('-o', '--options', required=True, type=int)
    parser.add_argument('-s', '--switch', action='store_true')
    parser.add_argument('-r', '--runs', default=1e5, type=int)
    return parser


def _monty_opens(current_option: int, correct_option: int, option_list: List[str]) -> int:
    available_options = [i for i in option_list if i not in [current_option, correct_option]]
    return random.choice(available_options)


def main(n: int, switch: bool, N: int = 1e06) -> float:
    """
    Checks the payoff of the strategy you follow on a game based
    on the Monty Hall problem.

    If you win in a run, this equals a $1 payoff, else you don't win anything
    (payoff is there $0 for that run.)

    Parameters
    ----------
    n : int
        Number of options each run.
    switch : bool
        If True, you switch after Monty revels an option.
    N: int, default: 1e06
        Number of runs in the game.
    
    Returns
    -------
    int
        Payoff for the game in $.

    Notes
    -----
    We assume, you always choose the first option in each run, because all options are
    equal probable. 
    """
    payoff: float = 0.0
    option_list: List[int] = [i for i in range(n)]
    for _ in range(N):
        current_option: int = 0
        correct_option: int = random.choice(option_list)
        open_option = _monty_opens(
            current_option=current_option,
            correct_option=correct_option,
            option_list=option_list,
        )
        if switch:
            available_options = [i for i in option_list if i not in [current_option, open_option]]
            current_option = random.choice(available_options)
        if current_option == correct_option:
            payoff += 1
    print(f'[SWITCH={switch}] Total payoff was {payoff} (P[WIN]={round(payoff/N, 4)} & N={N})')


if __name__ == '__main__':
    parser = _init_argparser()
    args = parser.parse_args()
    main(
        args.options,
        args.switch,
        args.runs,
    )
    