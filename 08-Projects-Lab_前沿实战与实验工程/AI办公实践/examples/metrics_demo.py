"""Synthetic arithmetic examples; no service benchmarking or real prices."""
import json
import math


def token_cost(input_tokens, output_tokens, input_per_million, output_per_million):
    if min(input_tokens, output_tokens, input_per_million, output_per_million) < 0:
        raise ValueError('all values must be nonnegative')
    return (input_tokens * input_per_million + output_tokens * output_per_million) / 1_000_000


def nearest_rank(values, percentile):
    if not values or not 0 < percentile <= 100:
        raise ValueError('nonempty values and percentile in (0,100] required')
    return sorted(values)[math.ceil(percentile / 100 * len(values)) - 1]


if __name__ == '__main__':
    print(json.dumps({'mode':'synthetic_not_real_prices_or_performance',
                      'cost_yuan':token_cost(1000,200,2,8),
                      'sample_count':3, 'ttft_p95_seconds':nearest_rank([0.4,0.6,1.2],95)}, indent=2))
