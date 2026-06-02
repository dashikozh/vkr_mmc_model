import math
class ModelMM1:
    
    def __init__(self, lam, mu, n):
        """
        Конструктор класса
        λ - Частота поступления запросов
        μ - Частота обслуживания сервером
        """
        self.lam= lam 
        self.mu = mu 
        self.n  = n 

    def is_valid(self):
        # μ должна быть больше λ
        return self.mu > self.lam
    
    def mm1(self):
        result = {
            'lam': self.lam,
            'mu':  self.mu,
            'n':  self.n,
            'models': 'mm1'
        }
        if not self.is_valid():
            result['log'] = '<span class="red">Значение <b>µ</b> должно быть больше <b>λ</b></span>'
            return result
        try:
            # Вероятность того, что система не занята
            P0 = self.lam / (self.lam + self.mu) # P0 = (λ / (λ + µ))
            
            # Среднее количество запросов в системе
            L = (self.lam / self.mu) / (1 - P0) # L = (λ / µ) / (1 - P0)
            
            # Среднее время в системе
            W = 1 / (self.mu - self.lam) # W = 1/(µ – λ) 
            # Вероятность того, что в системе будет n запросов
            Pn = (self.lam ** self.n) / math.factorial(self.n) * math.exp(-self.lam)  # Pn = (λⁿ / n!) × e⁻ˡ
            
            result.update({
                'P0':   f"{P0:.3f}",
                'L':    f"{L:.3f}",
                'W':    f"{W:.3f}",
                'Pn':   f"{Pn:.3f}",
                'state': 'true',
                'log': '<span class="green">Данные успешно рассчитаны (mm1)</span>'
            })
            return result
            
        except OverflowError:
            result['log'] = '<span class="red">Ошибка: слишком большое значение "c (количество серверов)"</span>'
            return result
