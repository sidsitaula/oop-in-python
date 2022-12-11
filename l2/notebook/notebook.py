import datetime


last_id = 0


class Note:
    """Represent note in a notebook. Match agains a string in seached and store tags for each note"""

    def __init__(self, memo, tags='') -> None:
        '''initialize a note with memo and optional space-separated tags. Automatically set note's creation date and a unique id'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter text. Returns true'''
        return filter in self.memo or filter in self.tags


class Notebook:

    def __init__(self):
        '''Initialize a notebook with empty list'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Creates new notes'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Find note by id '''
        for note in self.notes:
            if str(note_id) == str(note.id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find note by id and modify memo'''
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Find note by id and modify tags'''
        for note in self.notes:
            if note_id == note.id:
                note.tags = tags
                break

    def search(self, filter):
        '''searches notes according to filter passed.'''
        return [note for note in self.notes if note.match(filter)]
