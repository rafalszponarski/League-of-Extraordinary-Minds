from secret_base_of_horrible_baddies import get_secret_plan

# s�ownik przechowuj�cy zdobyte plany
stolen_plans = {}

def steal_plans(plan_list):
  # lista zawieraj�ca zdobyte plany
  stolen_plans_list = []

  # iteruj po elementach z plan_list
  for plan_number in plan_list:
    # je�eli plan o danym numerze nie zosta� jeszcze zdobyty,
    # u�yj get_secret_plan() do zdobycia planu
    if plan_number not in stolen_plans:
      plan = get_secret_plan(plan_number)

      # je�eli plan zosta� zdobyty, dodaj go do s�ownika stolen_plans
      if plan is not None:
        stolen_plans[plan_number] = plan

    # pobierz plan z s�ownika stolen_plans
    plan = stolen_plans[plan_number]

    # dodaj plan do listy stolen_plans_list
    stolen_plans_list.append(plan)

  # zwr�� list� zdobytych plan�w
  return stolen_plans_list
