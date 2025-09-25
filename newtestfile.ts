const coveredAuthors = await Promise.all(
        rawCoveredAuthors.map(async (author: any) => {
          try {
            if (!author?.commiter_name) return author; // no username available

            const userDetails = await getUserByUsername(
              githubToken,
              author.commiter_name
            );
            return {
              ...author,
              alias_name: userDetails.name || "",
            };
          } catch (error) {
            console.error(
              `Error fetching user details for ${author.name}:`,
              error
            );
            return author;
          }
        })
      );
