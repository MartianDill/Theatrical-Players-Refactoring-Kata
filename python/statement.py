import math
# обчислення вартості виніс у окремий метод calculate_amount
# прибрав метод format_as_dollars, тепер форматування безпосередньо при обчисленні result
# замінив play['type'] на play_type для кращої читабельності
# замінив perf['audience'] на audience для покращння читабельності та спрощення взаємодії
# замінив this_amount на amount для спрощення та схожості з іншими змінними
def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def calculate_amount(play_type, audience):
        if play_type == "tragedy":
            amount = 40000
            if audience > 30:
                amount += 1000 * (audience - 30)
        elif play_type == "comedy":
            amount = 30000
            if audience > 20:
                amount += 10000 + 500 * (audience - 20)
            amount += 300 * audience
        else:
            raise ValueError(f'unknown type: {play_type}')

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        play_type = play['type']
        audience = perf['audience']
        this_amount = calculate_amount(play_type, audience)

        # add volume credits
        volume_credits += max(audience - 30, 0)
        # add extra credit for every ten comedy attendees
        if play_type == "comedy":
            volume_credits += math.floor(audience / 5)
        # print line for this order
        result += f' {play["name"]}: ${this_amount/100:0,.2f} ({audience} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is ${total_amount/100:0,.2f}\n'
    result += f'You earned {volume_credits} credits\n'
    return result
