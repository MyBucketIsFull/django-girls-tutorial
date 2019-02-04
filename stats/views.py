from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ExecuteForm
import re
from stats.execute import Analyzer
from urllib.parse import urlencode


def execute_list(request):
    if request.method == "POST":
        form = ExecuteForm(request.POST)
        if form.is_valid():
            base_url = reverse('execute_list')
            query_string = urlencode({'input': form['input'].value()})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        get = request.GET.get('input')

        output = ''
        error = ''
        if get is not None:
            data = {'input': get}
            form = ExecuteForm(initial=data)

            analyzer = Analyzer()
            ints = [int(s) for s in re.findall(r'\d+', get)]

            if len(ints) > 0:
                output = {
                    'Maximum': analyzer.calculate_maxmimum(ints),
                    'Sum': analyzer.calculate_sum(ints),
                    'Mean': analyzer.calculate_mean(ints),
                    'Variance': analyzer.calculate_variance(ints),
                    'Standard Deviation': analyzer.calculate_standard_deviation(ints)
                }
            else:
                error = 'Fill in at least one integer.'
        else:
            form = ExecuteForm()

        return render(request, 'stats/execute_list.html', {'form': form, 'out': output, 'error': error})
