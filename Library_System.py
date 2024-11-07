from datetime import datetime

# Biblioteca
books = []
students = []
authors = []
loans = []
book_id_counter = 1 #Iniciar o contador de ID dos livros
author_id_counter = 1 #Iniciar o contador de ID dos autores
aluno_id_counter = 1 #Iniciar o contador de ID dos alunos

def createBook(title, author):
    dataAtual = datetime.now()
    global book_id_counter
    book = { 
      "id": book_id_counter,
      "title": title,
      "author": author,
      "isAvailable": True,
      "created_at": dataAtual,
      "updated_at": dataAtual
  }
    book_id_counter +=1
    return book

def createAuthor(name, dateBirth):
    global author_id_counter
    author = {
      "id": author_id_counter,
      "name": name,
      "dateBirth": dateBirth
  } 
    author_id_counter += 1
    return author

def createStudent(name,dateBirth,email):
    global aluno_id_counter
    aluno = {
        "id": aluno_id_counter,
        "name": name,
        "dateBirth": dateBirth,
        "email": email,
        "borrowed_books": []
    }
    aluno_id_counter += 1
    return aluno

def getBook(title_or_id):
    if len(books) == 0:
        print("--- Não existe livro cadastrado ---")
    else:
        for book in books:
            if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower() or book["author"]["name"].lower() == title_or_id.lower():
                status = "Disponivel" if book["isAvailable"] else "Emprestado"
                created_at = book["created_at"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"ID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nStatus: {status} \nData de Cadastro: {created_at}\n")
                return
        print("Livro não encontrado")

def editBooks(title_or_id):
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            new_title = input("Digite o novo titulo do livro: ")
            if new_title:
                book["title"] = new_title
                book["updated_at"] = datetime.now()
                print("- Livro atualizado com sucesso! -")
                return
    print("Livro não encontrado")

def deleteBooks(title_or_id):
    global books
    bookDelete = None

    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            bookDelete = book
            break

    if bookDelete:
        if confirm(f"Você tem certeza que deseja excluir o livro: {bookDelete['title']} (ID: {bookDelete['id']}) ?"):
            books.remove(bookDelete)
            print("--- Livro excluido com sucesso ---")
        else:
            print("--- Ação Cancelada ---")
    else:
        print("Livro não encontrado")

def listBooks():
    if len(books) == 0:
        print("--- Não existe livro cadastrado ---")
    else:
        for book in books:
            status = "Disponivel" if book["isAvailable"] else "Emprestado"
            created_at = book["created_at"].strftime("%d/%m/%Y %H:%M:%S")
            print(f"ID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nStatus: {status} \nData de Cadastro: {created_at}")

            if "updated_at" in book:
                updated_at = book ["updated_at"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"Ultima atualização: {updated_at}")

def listStudent():
    if len(students) == 0:
        print("--- Não existe aluno Cadastrado ---")
    else:
        for student in students:
            borrowed_books = student["borrowed_books"]
            borrowed_titles = []
            for book in books:
                if book["id"] in borrowed_books:
                    borrowed_titles.append(book["title"])
            borrowed_books_str = ', '.join(borrowed_titles) if borrowed_titles else "Nenhum livro emprestado"
            print(f"ID: {student['id']} \nNome: {student['name']} \nData de Nascimento: {student['dateBirth'].strftime("%d/%m/%Y")} \nE-mail: {student['email']} \nLivros Emprestados: {borrowed_books_str}\n")

def bookAvilable(title_or_id):
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            if book["isAvailable"]:
                print("Livro Disponivel para empréstimo")
                return True
            else:
                print("Livro não está disponível para empréstimo")
                return False
    print("Livro Não encontrado")
    return False

def loanBook(title_or_id, student_identifier):
    book_found = None
    for book in books: 
       if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
        book_found = book
        break

    if not book_found:
        print("Livro Não encontrado")
        return False
    if not book_found["isAvailable"]:
        print("O Livro não está disponível para empréstimo")
        return False

    student_found = None
    for student in students:
        if str(student["id"]) == student_identifier or student["name"].lower() == student_identifier.lower():
            student_found = student
            break

    if not student_found:
        print("Aluno não encontrado")
        return False

    loan = {
        "book_id": book["id"],
        "student_id": student["id"],
        "loan_date": datetime.now(),
        "return_date": None
    }
    loans.append(loan)
    book["isAvailable"] = False
    book["updated_at"] = datetime.now()
    student_found["borrowed_books"].append(book_found["id"])
    
    print("--- Empréstimo realizado com sucesso ---")
    return True

def returnBook(title_or_id):
    book_id = None
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            book_id = book["id"]
            break

    if book_id is None:
        print("Livro não encontrado")
        return

    for loan in loans:
        if loan["book_id"] == book_id and loan ["return_date"] is None:
            loan["return_date"] = datetime.now()

            for book in books:
                if book["id"] == book_id:
                    book["isAvailable"] = True
                    book["updated_at"] = datetime.now()

                    for student in students:
                        if student["id"] == loan["student_id"]:
                            student["borrowed_books"].remove(book_id)
                    print(f"--- Empréstimo do livro --- \nID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nEMPRÉSTIMO FINALIZADO!")
                    return
    print("Empréstimo não encontraddo ou já foi devolvido")

def listStudentHistory(student_identifier):
    student_found = None
    for student in students:
        if str(student["id"]) == student_identifier or student["name"].lower() == student_identifier.lower():
            student_found = student
            break
    if not student_found:
        print("Aluno não encontrado")
        return

    found_loans = None
    for loan in loans:
        if loan["student_id"] == student_found["id"]:
            found_loans = True

            book_found = None
            for book in books:
                if book["id"] == loan["book_id"]:
                    book_found = book
                    break

            loan_date = loan["loan_date"].strftime("%d/%m/%Y %H:%M:%S")
            return_date = loan["return_date"].strftime("%d/%m/%Y %H:%M:%S") if loan["return_date"] else "Livro Não Devolvido"

            if book_found:
                print(f"Livro: {book_found['title']} \nData do Empréstimo: {loan_date} \nData de Entrega: {return_date} \n")
    if not found_loans:
        print("Nenhum empréstimo encontrado para este aluno.")

def bookLoanHistory(book_identifier):
    book_found = None
    for book in books:
        if str(book["id"]) == book_identifier or book["title"].lower() == book_identifier.lower():
            book_found = book
            break
    if not book_found:
        print("Livro não encontrado")
        return

    found_loans = False
    for loan in loans:
        if loan["book_id"] == book_found["id"]:
            found_loans = True

            student_found = None
            for student in students:
                if student["id"] == loan["student_id"]:
                    student_found = student
                    break

            loan_date = loan["loan_date"].strftime("%d/%m/%Y %H:%M:%S")
            return_date = loan["return_date"].strftime("%d/%m/%Y %H:%M:%S") if loan["return_date"] else "Ainda Não Devolvido"

            if student_found:
                print(f"\nEmprestado para Aluno: {student_found['name']} (ID: {student_found["id"]}) \nData do Empréstimo: {loan_date} \nData de Entrega: {return_date}\n")
    if not found_loans:
        print("Nenhum empréstimo registrado para este livro")
#Função de repetição ValueError
def tryInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("--- Entrada inválida, insira um número inteiro ---")

def tryDate(prompt):
    while True:
        date_input = input(prompt)
        try:
            valid_date = datetime.strptime(date_input, "%d/%m/%Y")
            return valid_date
        except ValueError:
            print("--- Data inválida, insina a data no formato DD/MM/AAAA ---")
# Função de confirmação
def confirm(action):
    response = input(f"{action} (S/N): ").lower()
    return response == 's'

#Funções das condicionais
def cadastrarLivro():
    print("--- Cadastrar o livro ---")
    title = input("Digite o Titulo do livro: ")
    print("--- Cadastrar o Autor ---")
    name = input("Digite o nome do autor: ")
    dataBirth = tryDate("Digite a data de nascimento do Autor DD/MM/AAAA: ")
    author = createAuthor(name, dataBirth)
    authors.append(author)           
    book = createBook(title, author)
    books.append(book)
    print("--- Livro cadastrado com sucesso! ---")

def buscarLivro():
    title_or_id = input("Digite o titulo do Livro ou ID: ")
    getBook(title_or_id)

def editarLivro():
    title_or_id = input("Digite o titulo do Livro ou ID: ")
    editBooks(title_or_id)

def excluirLivro():
    title_or_id = input("Digite o titulo do livro ou ID: ")
    deleteBooks(title_or_id)

def cadastrarAluno():
    print("--- Cadastrar Aluno ---")
    name = input("Digite o nome do Aluno: ")
    dataBirth = tryDate("Digite a data de nascimento do Aluno DD/MM/AAAA: ")
    email = input("Digite o email do Aluno: ")
    student = createStudent(name,dataBirth,email)
    students.append(student)
    print("--- Aluno Cadastrado com sucesso ---")

def realizarEmprestimo():
    title_or_id = input("Digite o ID ou Título do livro para empréstimo: ")
    if bookAvilable(title_or_id):
        student_identifier = input("Digite o ID do Aluno ou nome do Aluno: ")
        if loanBook(title_or_id, student_identifier):
            print("--- Empréstimo registrado com sucesso ---")
        else:
            print("--- Falha ao registrar o empréstimo ---")
    else:
        print("--- Não é possivel realizar o empréstimo ---")

def finalizarEmpréstimo():
    title_or_id = input("Digite o ID do livro ou Título do livro para finalizar o empréstimo: ")
    returnBook(title_or_id)

def historicoEmprestimoAluno():
    listStudent()
    student_identifier = input("Digite o ID ou nome do Aluno para ver o histórico: ")
    listStudentHistory(student_identifier)

def historicoEmprestimoLivro():
    listBooks()
    book_identifier = input("Digite o ID do livro: ")
    bookLoanHistory(book_identifier)

def Menu():
    while True:
        print("\n--- Bem-vindo ao sistema da Biblioteca ---\n")
        print("1 .Cadastrar Livro")
        print("2 .Buscar Livro")
        print("3 .Editar Livro")
        print("4 .Excluir Livro")
        print("5 .Lista Livros")
        print("6 .Cadastrar Aluno")
        print("7 .Lista Alunos")
        print("8 .Realizar empréstimo")
        print("9 .Finalizar empréstimo")
        print("10 .Histórico de Empréstimo do Aluno")
        print("11 .Histórico de Empréstimo do Livro")
        print("12 .Sair \n")
        opcao = tryInput("Escolha uma opção: ")

        if opcao == 1:
            cadastrarLivro()

        elif opcao == 2:
            buscarLivro()
           
        elif opcao == 3:
            editarLivro()

        elif opcao == 4:
            excluirLivro()
            
        elif opcao == 5:
            listBooks()

        elif opcao == 6:
            cadastrarAluno()

        elif opcao == 7:
            listStudent()

        elif opcao == 8:
            realizarEmprestimo()

        elif opcao == 9:
            finalizarEmpréstimo()
        
        elif opcao == 10:
            historicoEmprestimoAluno()

        elif opcao == 11:
            historicoEmprestimoLivro()

        elif opcao == 12:
            print("--- Sistema Finalizado ---")
            break
        
        else:
            print("Opção Inválida, digite novamente.")
Menu()
